for r in range(1,5):
    for h in range(5,r, -1):
        print("  ", end= "  ")    
    for e in range(0,r):
        print("* ", end= "  ")            
    for a in range(1,r):
        print("* ",end= "  ")
    print()           

for r in range (5,0,-1):
    for c in range(5, r ,-1):
        print("  " , end= "  ")
    for a in range(0, r):
        print("* " , end= "  ")  
    for m in range (1, r):
       print("* " , end= "  ")
    
    print()    