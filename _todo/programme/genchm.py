# coding: latin-1
"""genchm.py : g�n�ration automatique du fichier d'aide chm"""
import genhelp
import os
htmlworkshop_path = "\"c:\\Program Files\\HTML Help Workshop\\hhc.exe\""

def g (s) :
    """ajoute des guillements autour d'une cha�ne de caract�res"""
    return "\"" + s + "\""
    
def genhhp (files, premierepage, titre, \
            hhp = "help.hhp", hhc = "help.hhc", hhk = "help.hhk") :
    """g�n�re le fichier hpp d�finissant le fichier d'aide chm,
    files est la liste des fichiers HTML
    premierepage est la page � afficher en premier
    titre est le titre de l'aide"""
    proj = """[OPTIONS]
Compatibility=1.1
Full-text search=Yes
Contents file=""" + hhc + """
Default Window=main
Default topic=""" + premierepage + """
Index file=""" + hhk + """
Language=0x40C French
Binary TOC=YES
Create CHI file=No
Title=""" + g (titre) + """

[WINDOWS]
main=""" + g (titre) + """, """ + g (hhc) + """, """ + g (hhk) + """ , """ + \
        g (premierepage) + """, """ + g (premierepage) + """,,,,,0x23520,,0x387e,,,,,,,,0

[FILES]
"""
    for f in files :
        proj += f + "\n"
        
    f = open (hhp, "w")
    f.write (proj)
    f.close ()
    
def gen_premierepage (files, titre, res = "index.html") :
    """g�n�re la premi�re page de l'aide au format HTML"""
    s = """<HTML><head><title>""" + titre + """</title></head><BODY>\n"""
    s += "<H1>" + titre + "</H1>\n"
    for f in files :
        s += "<A HREF=\"" + f + "\">" + f.replace (".html", "") + "</A><BR>\n"
    s += "</BODY></HTML>\n"
    
    f = open (res, "w")
    f.write (s)
    f.close ()
    
def genhh_input (entree, page, link = True) :
    """retourne la cha�ne de caract�res associ�e � une entr�e de la table des mati�res"""
    res = """<LI><OBJECT type="text/sitemap"><param name="Name" value=\"""" + entree + """\">"""
    if link : res += """<param name="Local" value=\"""" + page + """\">"""
    res += """<param name="ImageNumber" value="11"></OBJECT>\n"""
    return res
    
def genhhc (files, premierepage, titre, hhc = "help.hhc") :
    """g�n�re le fichier hhc, m�me param�tre que pour hhp"""
    res ="""<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML//EN"><HTML><HEAD></HEAD><BODY>
        <OBJECT type="text/site properties">
        <param name=""" + g (titre) + """ value="right">
        </OBJECT>
        <UL>"""
    res += genhh_input (titre, premierepage, False)
    res += "<UL>\n"
    res += genhh_input ("modules", premierepage, False)
    res += "<UL>\n"
    for f in files :
        res += genhh_input (f.replace (".html", ""), f)
    res += "</UL>\n"
    res += "</UL>\n"
    res += "</UL>\n"
    res += "</BODY></HTML>\n"
    
    f = open (hhc, "w")
    f.write (res)
    f.close ()

def genhhk (files, premierepage, titre, hhk = "help.hhk") :
    """g�n�re le fichier hhk, m�me param�tre que pour hhp"""
    res ="""<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML//EN"><HTML><HEAD></HEAD><BODY>
        <OBJECT type="text/site properties">
        <param name=""" + g (titre) + """ value="right">
        </OBJECT>
        <UL>"""
    res += genhh_input (titre, premierepage)
    res += "<UL>\n"
    for f in files :
        res += genhh_input (f.replace (".html", ""), f)
    res += "</UL>\n"
    res += "</UL>\n"
    res += "</BODY></HTML>\n"
    
    f = open (hhk, "w")
    f.write (res)
    f.close ()

def genchm (files, titre, \
            hhp = "help.hhp", hhc = "help.hhc", hhk = "help.hhk") :
    """g�n�re le fichier d'aide complet"""
    premierepage = "index.html"                     # g�n�re la page de garde
    gen_premierepage (files, titre, premierepage)   
    files.append (premierepage) 
    genhhp (files, premierepage, titre)             # g�n�re le fichier hhp
    genhhc (files, premierepage, titre)             # g�n�re le fichier hhc
    genhhk (files, premierepage, titre)             # g�n�re le fichier hhk
    os.system (htmlworkshop_path + " " + hhp)       # appelle HTML WorkShop en ligne de commande

if __name__ == "__main__" :
    files = [".\\genchm.py", ".\\genhelp.py", "os", "sys"]
    res   = genhelp.genhelp (files)
    print res  # ['genchm.html', 'genhelp.html', 'os.html', 'sys.html']   
    genchm (res, "GenHelp")