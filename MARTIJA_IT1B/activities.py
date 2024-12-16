from name import name
from age import age
from add import add
from fah import fah
from c import c

def activity2():
    print("hello world")
    print("---------------")   

def activity3():
    print("Hi,",name,"from",add,"age of",age)  
    
print(f"Hi,{name} from {add} age of {age}")    
print("---------------")    

def activity4():
    print(round(c,2))

import fah
print(f"{fah} degrees in Fahrenheit coverted to celsius is {round(c,2)}")
print("---------------")    

def activity5():  
    x = 10
    print(x)  

    x = x + 10
    print(x)

    x = x + 20
    print(x)

    x += 10
    print(x)

    x *= 3
    print(x)
    print("---------------")    


def activity6():	
	from password import password
password = "martija"	
mypassword = input("ENTER PASSWORD --->")


if password == mypassword.lower() :
	print("ACCESS GRANTED")
	print("ENJOY USING THE SYSTEM")

elif mypassword.lower() == "rhea":
	print("ACCESS GRANTED")
	print("ENJOY USING THE SYSTEM")
	print("---------------")

else:
	print("ACCESS DENIED ")
	print("---------------")

	
def activity7():
	prelim
prelim = eval(input("Enter your prelim grade:"))
midterm = eval(input("Enter your midterm grade:"))
semifinal = eval(input("Enter your semifinal grade:"))
final = eval(input("Enter your final grade:"))
quiz = eval(input("Enter your quiz grade:"))
project = eval(input("Enter your project grade:"))

ave = (prelim * 0.15) + (midterm * 0.15) + (semifinal * 0.15) + (final * 0.15) + (quiz *0.25) + (project * 0.15) / 6

print(ave)

if ave >=75 :
	print("CONGRATULATIONS!YOU PASSED THE COURSE!")
	print("---------------")

else:
	print("Sorry,you failed.")



activity2()
activity3() 
activity4()
activity5()
activity6()
activity7()