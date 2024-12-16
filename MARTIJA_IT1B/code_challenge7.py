name = input("Enter your name:")

grocery = input(f"Did you purchase a grocery today {name}?(yes/no)")
if grocery.lower() == "yes":
    print(f"Welcome to the grocery store {name}")
else:
    print("You need to purchase first.")

purchase = input("What did you purchase?")
purchase == 2100
if purchase:
         print("Item price:" , 2100)
else:
            print("Buy first.")

taxed = 0.123
total = 2100 + 0.123
print("Total with taxed:" , total)        

payment = eval(input("How much is your payment cash?"))
cash = payment

nodiscount = cash - total

age = eval(input("Enter your age:"))
if age >= 60 and age <=150:
             print("Congratulations you have a discount upto 12.3%!")  

             seniordiscount = 0.123
             senior = total - 0.123
             change1 = cash - senior
             print("Total change for senior:" , change1)

else:
            print("Invalid for discount,maybe next time if you're already senior.") 

if payment == 4000 and total <= 4000:
    print("Congratulations,because your grocery reach more than 4000 you have a coupon!")

    coupon = 0.038
    cash1 = purchase - 0.038
    change2 = cash - cash1
    print("Total change if you have coupon:" , change2)

else:
    print("You dont reach the minimum of the total,you cannot avail discount. ")   

print("Total change if you dont have any discount:" , nodiscount)    

print(f"Thank you for shopping {name},shop again next time.")
