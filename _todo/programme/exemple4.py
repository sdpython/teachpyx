alias = __import__ ("module_exemple")

c = alias.exemple_classe ()
print c
print alias.exemple_fonction ()
help (alias)