class CreationDestruction (object) :
    
    def __init__ (self) :
        print("constructeur")
        
    def __new__ (self) :
        print("__new__")
        return object.__new__ (self)
        
    def __del__ (self) :
        print("__del__")

print("a")
m = CreationDestruction ()
print("b")
m2 = m
print("c")
del m
print("d")
del m2
print("e")
