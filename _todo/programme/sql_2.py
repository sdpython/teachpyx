import sqlite3 as SQL
cx = SQL.connect("madatabase.db3")
cur = cx.cursor()

cur.execute ("""INSERT INTO ELEVE (nom, prenom, date, adresse, codepays, classe)
                VALUES ('dupre', 'xavier', '11/08/1975', '---- paris', 33, 19) ;""")
cur.execute ("""INSERT INTO ELEVE (nom, prenom, date, adresse, codepays, classe)
                VALUES ('dupre', 'gilles', '24/12/1946', '---- charleville', 33, 56) ;""")
cx.commit ()