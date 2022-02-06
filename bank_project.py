global balance
balance = 2000


def deposite(amount):
    global balance
    balance += amount
    return balance


def windrow(amount):
    global balance
    balance -= amount
    return balance


print("windrowal amount is:- ",windrow(10))
print("deposite amount is :-",deposite(100))