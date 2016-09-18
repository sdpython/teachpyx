import odbc
cx = odbc.odbc("mysqlperso")
cur = cx.cursor()

cur.execute ("""INSERT INTO ELEVE (num, nom, prenom, date, adresse, codepays, classe)
                VALUES (1, 'dupre', 'xavier', '1975-08-11', '---- paris', 33, 19) ;""")
cur.execute ("""INSERT INTO ELEVE (num, nom, prenom, date, adresse, codepays, classe)
                VALUES (2, 'dupre', 'gilles', '1946-12-24', '---- charleville', 33, 56) ;""")
cx.commit ()