balance = 50
print("Amount Due:", balance)
while balance <= 50 and balance > 0:
    coins = int(input("Insert coins: "))
    if coins == 10 or coins == 25 or coins == 5:
        balance -= coins
        if balance > 0:
            print("Amount Due: ", balance)
    else:
        print("Amount Due: ", balance)

if balance < 0:        
    print("Change Owed:", abs(balance))
if balance == 0:
    print("Change Owed: 0")