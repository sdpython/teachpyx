def fonction_somme_list (ens) :
    r = "list "
    for e in ens : r += e
    return r

def fonction_somme_dict (ens) :
    r = "dict "
    for k,v in ens.items () : r += v
    return r

def fonction_somme (ens) :
    if   isinstance (ens, dict) : return fonction_somme_dict (ens)
    elif isinstance (ens, list) : return fonction_somme_list (ens)
    else                        : return "erreur"
        
li = ["un", "deux", "trois"]
di = {1:"un", 2:"deux", 3:"trois"}
tu = ("un", "deux", "trois")
print(fonction_somme(li))  # affiche list undeuxtrois
print(fonction_somme(di))  # affiche dict undeuxtrois
print(fonction_somme(tu))  # affiche erreur