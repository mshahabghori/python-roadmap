print("MENU")
choice=int(input("Enter your choice\n1-Check Balance\n2-Deposit Money\n3-Wihdraw Money\n4-Exit\n"))
match choice:
    case 1:
        print("Checking Balance")
    case 2:
        print("Depositing Money")
    case 3:
        print("Withdrawing Money")
    case 4:
        print("Exiting")
    case _:
        print("Invalid Choice")