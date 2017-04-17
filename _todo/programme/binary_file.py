# coding: latin-1
import struct
# on enregistre un entier, un r�el et 4 caract�res
i = 10
x = 3.1415692
s = "ABCD"

# �criture
with open ("info.bin", "wb") as fb:
    fb.write ( struct.pack ("i" , i) )
    fb.write ( struct.pack ("d" , x) )
    octets = s.encode("ascii")
    fb.write ( struct.pack ("4s" , octets) )

# lecture
with open ("info.bin", "rb") as fb:
    i = struct.unpack ("i",   fb.read (4))
    x = struct.unpack ("d",   fb.read (8)) 
    s = struct.unpack ("4s",   fb.read (4))

# affichage pour v�rifier que les donn�es ont �t� bien lues
print(i)  # affiche (10,)
print(x)  # affiche (3.1415692000000002,)
print(s)  # affiche (b'ABCD',)