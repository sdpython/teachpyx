# coding: latin-1
import struct
# on enregistre un entier, un r�el et n caract�res
i = 10
x = 3.1415692
s = "ABCDEDF"

# �criture
file = open ("info.bin", "wb")
file.write ( struct.pack ("i" , i) )
file.write ( struct.pack ("d" , x) )
file.write ( struct.pack ("i" , len(s)) )  # on sauve la dimension de s
file.write ( struct.pack ("c" * len(s) , *s) )
file.close ()

# lecture
file = open ("info.bin", "rb")
i = struct.unpack ("i",      file.read (4)) 
x = struct.unpack ("d",      file.read (8)) 
l = struct.unpack ("i",      file.read (4)) # on r�cup�re la dimension de s
l = l [0]  # l est un tuple, on s'int�resse � son unique �l�ment
s = struct.unpack ("c" * l,  file.read (l)) 
file.close ()

# affichage pour contr�ler
print i  # affiche (10,)
print x  # affiche (3.1415692000000002,)
print s  # affiche ('A', 'B', 'C', 'D', 'E', 'D', 'F')