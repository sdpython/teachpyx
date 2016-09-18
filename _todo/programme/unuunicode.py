# coding: latin-1
st =  "eé"
su = u"eé"  # raccourci pour su = unicode ("eé", "latin-1")
print len (st),        ";", st        # affiche  2 ; eé
print len (repr (st)), ";", repr (st) # affiche  7 ; 'e\xe9'
print len (su),        ";", su.encode ("latin-1")        # affiche  2 ; eé
print len (repr (su)), ";", repr (su) # affiche  8 ; u'e\xe9'
