#introduction to decision structures
#in some programming language or tutorials, its reeferred to as
#conditional statement or selection statement

password = "martija"

mypassword = input("ENTER PASSWORD --->")

# == / is equal to / its asking a question

if password == mypassword.lower() :
	print("ACCESS GRANTED")
	print("ENJOY USING THE SYSTEM")

elif mypassword.lower() == "rhea":
	print("ACCESS GRANTED")
	print("ENJOY USING THE SYSTEM")

else:
	print("ACCESS DENIED")