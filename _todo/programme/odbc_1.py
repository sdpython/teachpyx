import odbc
cx = odbc.odbc("mysqlperso")
cur = cx.cursor()

cur.execute ("""
CREATE TABLE ELEVE (
     num integer primary key,
     nom varchar (30),
     prenom varchar (30),
     date date,
     adresse varchar (100),
     codepays integer,
     classe integer)
""")