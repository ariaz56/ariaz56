balance=10000

print("Welcome to ATM")
pin=input("Enter PIN:")

if pin=="8520":

    print("\n1.Balance")
    print("2.Deposite")
    print("3.Withdraw")

    choice=int(input("Enter Choice:"))

    if choice==1:
        print("Balance=",balance)

    elif choice==2:
        amount=float(input("Deposite Amount:"))
        balance+=amount
        print("Updated Balance=",balance)

    elif choice==3:
        amount=float(input("Withdraw Amount:"))
        if amount<=balance:
            balance-=amount
            print("Updated Balance=",balance)

    else:
        print("Insufficien Balance.")

else:
    print("Invalid PIN")