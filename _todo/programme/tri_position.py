tab = ["z�ro", "un", "deux"]                        # tableau � trier
pos = [ (tab [i],i) for i in range (0, len (tab)) ] # tableau de couples
pos.sort ()                                         # tri    
print pos                # affiche [('deux', 2), ('un', 1), ('z�ro', 0)]