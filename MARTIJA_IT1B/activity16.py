#while loop
#types of loop


tuloy = True

sum = 0
while tuloy == True:
    num = eval(input("Enter any number:"))

    if num == 0:
        print("Loop ended")
        sum += num
        print(f"The sum f all the number given is {sum}")
        break
    else:
        sum += num
        continue