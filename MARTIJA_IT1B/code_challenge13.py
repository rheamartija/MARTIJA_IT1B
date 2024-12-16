con = True
sum = 0

while con == True:
    num= eval(input("Enter a number:"))

    if num == 0:
        print("Loop has ended")
        print(f"The sum of the given number is {sum}")
        break
    else:
        sum += num
        continue