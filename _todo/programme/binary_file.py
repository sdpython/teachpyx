# coding: latin-1
import struct
# on enregistre un entier, un r�el et 4 caract�res
i = 10
x = 3.1415692
s = "ABCD"

# �criture
file = open ("info.bin", "wb")
file.write ( struct.pack ("i" , i) )
file.write ( struct.pack ("d" , x) )
file.write ( struct.pack ("cccc" , *s) )
file.close ()

# lecture
file = open ("info.bin", "rb")
i = struct.unpack ("i",      file.read (4)) 
x = struct.unpack ("d",      file.read (8)) 
s = struct.unpack ("cccc",   file.read (4)) 
file.close ()

# affichage pour v�rifier que les donn�es ont �t� bien lues
print i  # affiche (10,)
print x  # affiche (3.1415692000000002,)
print s  # affiche ('A', 'B', 'C', 'D')