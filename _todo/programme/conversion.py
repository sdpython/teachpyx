import py2html
import os
import os.path

py_page = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1 (Latin-1)" >
<title>%s</title>
<style type="text/css">
    h1 {    color: green;
            position: center;
        }
    .python_code {  font-family: monospace;
                font-size: 10pt;
                }
    .py_key {color: black;}
    .py_num color: black;{}
    .py_str { color: #00AA00;}
    .py_op {color: black; }
    .py_com { color: red;}
    .py_res { color: #FF7700;}
    .py_def { color: blue;}
    .py_brk { color: black;}
</style>
</head>
<body>
<h1>Programme %s</h1>
<hr>
%s
<hr>
créé avec py2html version:%s
<p>
</p></body>
</html>"""

l = os.listdir ("")
for f in l:
    racine,ext = os.path.splitext (f)
    if ext == ".py":
        print "conversion of ", f
        appliedstyle    = py2html.readStyleFile(None)
        data            = py2html.file2HTML(f,"0",appliedstyle,False,"1")
        block           = py2html.makeBlock (data)
        html            = py_page % (f,f,block,py2html.__version__)
        outfile         = racine + ".html"
        file            = open(outfile,"w")
        file.write(html)
        file.close()
print "end"