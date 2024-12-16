num = eval(input("Enter a number:"))

for x in range(1,11):
    for y in range(1,num +1):
        print(f"{x} * {y} = {x + y}",end= " " )

    print()    