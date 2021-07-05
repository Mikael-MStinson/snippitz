from unittest import TestCase
from database_tools import *

class TestDataBase(TestCase):
	def test_create_table(self):
		command = create(table("test"))
		self.assertEqual(command, "CREATE TABLE test;")
		
	def test_create_table_with_a_column(self):
		command = create(table("test",integer("id")))
		self.assertEqual(command, "CREATE TABLE test (id integer);")
		
	def test_create_table_with_multiple_columns(self):
		command = create(table("test",integer("id"),integer("value"),integer("some_numbers")))
		self.assertEqual(command, "CREATE TABLE test (id integer, value integer, some_numbers integer);")
		
	def test_create_database(self):
		command = create(database("test"))
		self.assertEqual(command, "CREATE DATABASE test;")
	
	def test_select_all(self):
		command = select(all(),from_table("test"))
		self.assertEqual(command, "SELECT * FROM test;")
		
	def test_select_column(self):
		command = select(column("test"),from_table("test"))
		self.assertEqual(command, "SELECT test FROM test;")
		
	def test_select_columns(self):
		command = select(column("a"),column("b"),column("c"),from_table("test"))
		self.assertEqual(command, "SELECT a, b, c FROM test;")
		
	def test_select_all_conditionally(self):
		command = select(all(),from_table("test"),where(equal(column("test"),"blah")))
		self.assertEqual(command, "SELECT * FROM test WHERE test == blah;")