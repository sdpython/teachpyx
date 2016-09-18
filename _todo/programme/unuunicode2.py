# coding: utf-8
s = unicode ("été".decode ("utf-8"))
print len (s), s.encode ("utf-8")
print len (repr (s)), repr (s)

s = u"ete"
print len (s), s
print len (repr (s)), repr (s)
