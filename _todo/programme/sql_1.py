import sqlite3 as SQL
cx = SQL.connect("madatabase.db3")
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