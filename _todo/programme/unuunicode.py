# coding: latin-1
st =  "e�"
su = u"e�"  # raccourci pour su = unicode ("e�", "latin-1")
print len (st),        ";", st        # affiche  2 ; e�
print len (repr (st)), ";", repr (st) # affiche  7 ; 'e\xe9'
print len (su),        ";", su.encode ("latin-1")        # affiche  2 ; e�
print len (repr (su)), ";", repr (su) # affiche  8 ; u'e\xe9'
