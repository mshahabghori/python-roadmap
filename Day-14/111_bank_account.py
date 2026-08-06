class BankAccount:
    pass

account_01=BankAccount()

account_01.name="Shahab"
account_01.account_no=123456789
account_01.balance=5000

print("Name =",account_01.name)
print("Account Number =",account_01.account_no)
print("Balance =",account_01.balance)

choice=input("Do you want to deposit or withdraw :").lower()

if choice=="deposit":
    saving=int(input("Enter amount :"))
    account_01.balance=account_01.balance+saving

elif choice=="withdraw":
    saving=int(input("Enter amount :"))

    if saving <= account_01.balance:
        account_01.balance=account_01.balance-saving
    else:
        print("Insufficient Balance")
else:
    print("Invalid Input")

print("Updated Balance =",account_01.balance)