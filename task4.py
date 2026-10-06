"""
age=int(input("enter the age of  the person:"))
ID=input("Is your id Valid(Yes or No):")
if age>=18:
    if ID=="Yes":
        print("You are eligible")
    else:
        print("You are not eligible")
else:
    print("You are underage")

"""
"""
ogpin="8055"
balance=200000
pin=input("enter u r pin:")
if pin == ogpin:
    amount=float(input("enter withdrawal amount:"))
    if amount <= balance:
        print("Successful")
        print("Remaining balance",balance-amount)
    else:
        print("Insufficient balance")
else:
    print("Incorrect Pin")
"""

"""
n=int(input("Enter the first Number: "))
m=int(input("Enter the second number: "))
op=input("Enter the operator: ")
match(op):
    case '+':
        print("The sum is ",n+m)
    case'-':
        if n>=m:
            print("The difference is ",n-m)
        else:
            print("The difference is ",m-n)
    case'*':
        print("The product is ",n*m)
    case'/':
        print("The quotient is ",n/m)
    case _:
        print("Invalid operator")
"""
"""
balance=20000
n=int(input("1.Deposit    2.Withdraw   3.balance  :   "))
match (n):
    case 1:
        n1=int(input("Enter the amount to deposit  :  " ))
        balance+=n1
        print("The balance amount is ",balance)
    case 2:
        n2=int(input("Enter the amount to withdraw  :  " ))
        if balance>=n2:
                print("money granted")
                balance-=n2
                print("balance is ",balance)
        else:
            print("Not sufficient balance")
    case 3:
        print("The balance amount is ",balance)
    case _:
          print("Invalid")
"""