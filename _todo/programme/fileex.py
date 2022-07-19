    
for i in range(0, 5):
    try :
        x, y = i-1, i-2
        print(f"{x}/{y}")
        with open("essai.txt", "a") as f:
            f.write(f"{x}/{y}=")
            f.write(str((float (x)/y)) + "\n" )     # exception si y == 0
    except Exception as e: 
        print("erreur avec i = ", i, ",", e, f.closed)