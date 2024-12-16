#MARTIJA 1B
#DENOMINATIONS

name = input("Hi,Input your name:")
amount = eval(input("Enter amount to deposit:"))

print("Hi" , name ,"your deposit amount breakdown in PH denominators is as follows:")

ans1 = amount//1000
amount = amount % 1000
print(ans1, 1000)

ans2 = amount // 500
amount = amount % 500
print(ans2,500)

ans3 = amount // 200
amount = amount % 200
print(ans3,200)

ans4 = amount // 100
amount = amount % 100
print(ans4,100)

ans5 = amount // 50
amount = amount % 50
print(ans5,50)

ans6 = amount // 20 
amount = amount % 20
print(ans6,20)

ans7 = amount // 10
amount = amount % 10
print(ans7,10)

ans8 = amount // 5
amount = amount % 5
print(ans8,5)

ans9 = amount // 1
amount = amount % 1
print(ans9,1)
