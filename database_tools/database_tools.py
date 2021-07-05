def scrub(value):
	keywords = ['ADD','ALTER','AND','ANY','AS','ASC','BACKUP','BETWEEN','CASE','CHECK','COLUMN','CONSTRAINT','CREATE','REPLACE','DATABASE','DEFAULT','DELETE','DESC','DROP','EXEC','EXISTS','FOREIGN','KEY','FROM','FULL','GROUP','HAVING','IN','INDEX','INSERT','IS','NULL','JOIN','LEFT','LIKE','LIMIT','NOT','OR','ORDER','BY','OUTER','PRIMARY','PROCEDURE','RIGHT','ROWNUM','SELECT','DISTINCT','INTO','SET','TABLE','TOP','TRUNCATE','UNION','ALL','UNIQUE','UPDATE','VALUES','VIEW','WHERE']
	for keyword in keywords:
		if keyword in value:
			raise Exception("SQL commands detected in value {}").format(value)
	return value

def create(item):
	return "CREATE {};".format(item)
	
def table(name, *columns):
	if len(columns) == 0:
		return "TABLE {}".format(scrub(name))
	else:
		return "TABLE {} ({})".format(name, ", ".join(columns))
			
def integer(name):
	return "{} integer".format(scrub(name))
	
def database(name):
	return "DATABASE {}".format(scrub(name))
	
def select(*args):
	return "SELECT {} {};".format(", ".join(args[:-1]),args[-1])
	
def all():
	return "*"
	
def from_table(name):
	return "FROM {}".format(scrub(name))
	
def column(name):
	return scrub(name)
