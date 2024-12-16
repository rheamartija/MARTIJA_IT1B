sum = 0
even = 0
odd = 0

for x in range (1,11):
    num = eval(input(f"Enter #{x} :"))
    sum += num

    if num % 2 :
        even += num
    else:
        odd + num

print(f"The sum of all the numbers given is {sum}")
print(f"The sum of all the even numbers ony is {even} ") 
print(f"The sum of all the odd numbers only is {odd}")           
