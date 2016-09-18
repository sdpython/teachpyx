from pdftools.pdffile import PDFDocument
from pdftools.pdftext import Text

def contents_to_text (contents):
    for item in contents:
        if isinstance (item, type ([])):
            for i in contents_to_text (item):
                yield i
        elif isinstance (item, Text):
            yield item.text

doc = PDFDocument ("declaration.pdf")
n_pages = doc.count_pages ()
text = []

for n_page in range (1, (n_pages+1)):
    print "Page", n_page
    page = doc.read_page (n_page)
    contents = page.read_contents ().contents
    text.extend (contents_to_text (contents))

print "".join (text)

f = open ("ok.txt", "w")
f.write ("".join (text))
f.close ()
