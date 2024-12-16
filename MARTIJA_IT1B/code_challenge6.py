name = input("Enter your name:")
age = eval(input("Enter your age:"))


if age >= 1 and age <= 8:
	print("Toddler")
else: 
	print("invalid")

if age >= 9 and age <= 14:
	print("Pre-teen")
else: 
	print("invalid")

if age >= 15 and age <= 18:
	print("Teenager")
else: 
	print("invalid")

if age >= 19 and age <= 27:
	print("Early Adulthood")
else: 
	print("invalid")

if age >= 28 and age <= 44:
	print("Middle Age")
else: 
	print("invalid")

if age >= 45 and age <= 59:
	print("Post Adulthood")
else: 
	print("invalid")

if age >= 60 :
	print("Senior")
else: 
	print("invalid")
