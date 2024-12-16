import os
con = True 

nt = 0
while con == True:
    ask = input("Do you want to print more triangle (yes/no):")

    if ask.lower() == "no":
        print("Loop has ended")
        break

    elif ask.lower() == "yes":
        os.system('cls')
        nt += 1
        for r in range(1,6):
            for h in range(1,nt + 1):
                for e in range(1,r +1):
                    print("*",end= " ")
                for a in range(6,r ,-1):
                    print(" ",end= " ")    
                print(end= " ")
            print()
        continue
    else:
        print("INVALID")
        print("Enter yes/no")  

 
