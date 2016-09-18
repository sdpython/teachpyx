mat = ["Victor Hugo 6".split (), "Marcel Proust 3".split () ]
f = open ("tableau.html", "w")
f.write ("<body><html>\n")
f.write ("<table border=\"1\">\n")
for m in mat :
    f.write ("<tr>")
    for c in m :
        f.write ("<td>" + c + "</td>")
    f.write ("</tr>\n")
f.write ("</table>")
f.close ()

import os
os.system ("\"C:\\Program Files\\Mozilla Firefox\\firefox.exe\" tableau.html")
os.system ("\"C:\\Program Files\\Internet Explorer\\iexplore.exe\"" \
           " d:\\temp\\tableau.html")