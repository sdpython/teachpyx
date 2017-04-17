# coding: latin-1
import struct
# on enregistre un entier, un réel et n caractères
i = 10
x = 3.1415692
s = "ABCDEDF"

# écriture
with open ("info.bin", "wb") as fb:
    fb.write ( struct.pack ("i" , i) )
    fb.write ( struct.pack ("d" , x) )
    r = s.encode("utf-8")
    fb.write ( struct.pack ("i" , len(r)) )  # on sauve la dimension de r
    fb.write ( struct.pack ("{0}s".format(len(r)), r) )

# lecture
with open ("info.bin", "rb") as fb:
    i = struct.unpack ("i", fb.read (4)) 
    x = struct.unpack ("d", fb.read (8)) 
    size = struct.unpack ("i", fb.read (4)) # on récupère la dimension de s
    size = size [0]  # l est un tuple, on s'intéresse à son unique élément
    s = struct.unpack ("{0}s".format(size), fb.read (size)) 

# affichage pour contrôler
print(i)
print(x)
print(s)

from struct import pack
print(len(pack('i', 0)))
print(len(pack('d', 0)))
print(len(pack('s', b'0')))
