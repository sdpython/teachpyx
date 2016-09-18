# coding: latin-1
import odbc 
cx = odbc.odbc("mysqlperso")
cur = cx.cursor()

cur.execute ("SELECT * from ELEVE") 
for row in cur.fetchall () :
    print [ str (r) for r in row ]