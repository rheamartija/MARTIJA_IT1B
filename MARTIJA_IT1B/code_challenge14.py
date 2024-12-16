#Bank Simulation Program
Bank = 1


def bank_greet ():
    print("Hi,Welcome to this Bank.")

def bank_denominations(amount):
    thousand = amount // 1000
    thou1 = amount % 1000

    fhundred = thou1 // 500
    fhun1 = thou1 % 500

    thundred = fhun1 // 200
    thun1 = fhun1 % 200

    ohundred = thun1 // 100
    ohun1 = thun1 // 100

    fifty = ohun1 // 50
    fif1 = ohun1 // 50

    twenty = fif1 // 20
    twen1 = fif1 // 20

    ten = twen1 // 10
    ten1 = twen1 // 10

    five = ten1 // 5
    five1 = ten1 // 5

    one = five1 // 1
    one1 = five1 // 1

def bank_account():
    print("Welcome!Let's create your account!")    
    name = input("Enter your name:")
    balance = 0
    print(f"Bank Account succesfully created for {name}!")        
    return name , balance
        
def bank_deposit(balance):
    print("Deposit")
    amount = eval(input("Enter the amount to deposit:"))
    bank_denominations(amount)
    balance += amount
    print(f"Succesfully deposit!Your new balance is:PHP {balance}")
    return balance

def bank_withdraw (balance):
    print("Withdraw")
    amount = eval(input("Enter the amount to withdraw:"))
    if amount > balance:
        print("Insufficient balance,transaction failed!")
    else:
        balance -= amount
        print(f"Succesfully withdraw!Your new balance is:PHP{balance}")    
        return balance

def bank_balance(balance):
    print(f"Your current balance is:PHP{balance}")       

def bank_main():
    name,balance = bank_account()
    while True:
        print("-------------------------")
        print("\n Bank Menu:")
        print("1--Deposit")
        print("2--Withdraw")
        print("3--Check Balance")
        print("4--Exit")

        choice = int(input("Select an option(1,2,3,4):"))
        if choice == 1:
            balance = bank_deposit(balance)
            continue
        elif choice == 2:
            balance = bank_withdraw(balance)
            continue
        elif choice == 3:
            bank_balance(balance)
            continue
        elif choice == 4:
            print(f"Goodbye,{name}!Thank your for choosing to bank with us.")
            break    
        else:
            print("Invalid choice,Please try again!")  

bank_denominations()
bank_main()
