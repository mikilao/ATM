
from banking_pkg import account


def atm_menu(name):

    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("Automatic Teller Machine")
name = input("Enter name to register: ")
pin = input("Enter PIN: ")
balance = "0"

print(name + " has been registered with a starting balance of $" + balance)
print("LOGIN")


while True:
    print("Please log in")

    name_to_validate = input("Username:")
    pin_to_validate = input("user PIN:")
    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful! ")
        break
    else:
        print("Invalid Credentials")
        break
while True:
    atm_menu(name)
    option = input("Choose an option: ")

    if option == '1':
        print(balance)

    elif option == "2":
        balance = account.deposit(balance)
        print("Your balance is now: ", balance)

    elif option == "3":

        print("Your account balance is now : ",
              balance - account.withdraw(balance))
    elif option == "4":
        account.logout(name)
        break
    else:
        print("Invalid option")
