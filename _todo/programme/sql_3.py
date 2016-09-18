# coding: latin-1
import sqlite3 as SQL
cx = SQL.connect("madatabase.db3")
cur = cx.cursor()

if False :
    #cur.execute ("INSERT INTO PAYS (codepays, pays) VALUES (33, 'France')")
    #cur.execute ("INSERT INTO PAYS (codepays, pays) VALUES (44, 'Royaume-Uni')")

    #cur.execute ("INSERT INTO MATIERES (matiere, num) VALUES ('français', 1)")
    #cur.execute ("INSERT INTO MATIERES (matiere, num) VALUES ('mathématiques', 2)")
    #cx.commit()

    if False :
        cur.execute ("INSERT INTO NOTE (nume,numm,note) VALUES (1,1,12)")
        cur.execute ("INSERT INTO NOTE (nume,numm,note) VALUES (1,1,14)")
        cur.execute ("INSERT INTO NOTE (nume,numm,note) VALUES (1,2,16)")
        cur.execute ("INSERT INTO NOTE (nume,numm,note) VALUES (1,2,8)")
        cur.execute ("INSERT INTO NOTE (nume,numm,note) VALUES (1,2,12)")

        cur.execute ("INSERT INTO NOTE (nume,numm,note) VALUES (2,1,8)")
        cur.execute ("INSERT INTO NOTE (nume,numm,note) VALUES (2,1,9)")
        cur.execute ("INSERT INTO NOTE (nume,numm,note) VALUES (2,2,11)")
        cur.execute ("INSERT INTO NOTE (nume,numm,note) VALUES (2,2,8)")
        cur.execute ("INSERT INTO NOTE (nume,numm,note) VALUES (2,2,12)")

        cx.commit ()


    import sqlite3 as SQL
    cx = SQL.connect("madatabase.db3")
    cur = cx.cursor()
    cur.execute("select * from NOTE")
    l = []
    for row in cur.fetchall(): 
        l.append (row)
        print row
    print l
    
print "-------------"
cur.execute ("select * from ELEVE")
for row in cur.fetchall(): print row

print "-------------"
req = """
SELECT nom,prenom,AVG(note) FROM ELEVE,NOTE
WHERE num = nume and 
      numm IN ( SELECT num FROM MATIERES WHERE matiere = 'français' ) 
GROUP BY nume
"""
cur.execute (req)
for row in cur.fetchall(): print row

print "-------------"
req = """
SELECT nom,prenom,AVG(note) FROM ELEVE,NOTE
WHERE num = nume and 
      numm IN ( SELECT num FROM MATIERES WHERE matiere = 'français' ) 
GROUP BY nume
HAVING AVG(note) >= 10
"""
cur.execute (req)
for row in cur.fetchall(): print row
