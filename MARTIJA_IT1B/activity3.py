#string formatting
#Bio Data Program
#to concentrate the 3 inputs to form a singular print

name = input("Please Enter your name --->")
add = input("Please Input your Address --->")
age = eval(input("Enter your age --->"))

print("Hi,",name,"from",add,"age of",age)

#string formatting

print(f"Hi,{name} from {add} age of {age}")