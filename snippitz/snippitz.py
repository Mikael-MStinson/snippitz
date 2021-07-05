import sqlite3

class Snippitz:
	def __init__(self, database):
		self.database = sqlite3.connect(database)
		self.cursor = self.database.cursor()
		self.cursor.execute("CREATE TABLE connections (subject_id integer, relative_id integer); CREATE TABLE values (id integer, value text)")
		self.database.commit()
		
	def open(self):
		pass
		
	def close(self):
		self.database.close()
		
	def __get_id_of_value(self, value):
		self.cursor.execute("SELECT id FROM values WHERE value='{}'".format(value))
		values = self.cursor.fetchall()
		if len(values) > 1:
			raise Exception("__get_id_of_value Multiple items with the same value")
		return values[0]
		
	def __get_value_of_id(self, id):
		self.cursor.execute("SELECT value FROM values WHERE id='{}'".format(id))
		return self.cursor.fetchall()[0]

	def tie(self, fileA, fileB):
		if fileA == fileB: return
		try:
			if fileB in self.list(fileA): return
		except FileNotFoundError:
			pass
		self.cursor.execute("INSERT INTO connections VALUES ('{}', '{}')".format(fileA, fileB))
		self.cursor.execute("INSERT INTO connections VALUES ('{}', '{}')".format(fileB, fileA))
		self.database.commit()
		
	def list(self, file):
		self.cursor.execute("SELECT * FROM connections WHERE file='{}'".format(file))
		l = self.cursor.fetchall()
		if l == []:
			raise FileNotFoundError("The file {} is not registered with Snippitz".format(file))
		return [i[1] for i in l]
		
	def severe(self, fileA, fileB):
		self.cursor.execute("DELETE FROM connections WHERE file='{}' AND relative='{}'".format(fileA, fileB))
		self.cursor.execute("DELETE FROM connections WHERE file='{}' AND relative='{}'".format(fileB, fileA))
		self.database.commit()
		
	def merge(self, fileA, fileB):
		fileA_connections = self.list(fileA)
		fileB_connections = self.list(fileB)
		for connection in fileA_connections:
			self.tie(fileB, connection)
		for connection in fileB_connections:
			self.tie(fileA, connection)
			
	def delete(self, file):
		connections = self.list(file)
		for connection in connections:
			self.severe(file, connection)