def deposit(balance):
    amount = input("Enter amount to deposit :  $")
    new_balance = int(balance + amount)
    return new_balance


def withdraw(balance):
    amount_taken = input("Enter amount to withdraw :  $")
    newer_balance = int(amount_taken - balance)
    return newer_balance


def logout(name):
    print("Goodbye " + name)
