#This is a Bank Project to understand the concept of Encapsulation in Python. 
#The BankAccount class has a private variable __balance to store the balance of the account and getter and setter methods to access and modify the balance. 
# The user can create an account, check account details, deposite amount and withdraw amount using the menu-driven interface.

class BankAccount():
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   # private variable to store the balance of the account
    
    def get_balance(self):     # getter method to access the private variable __balance
        return self.__balance
    
    def deposit(self, amount):    # setter method to modify the private variable __balance
        if amount > 0:
            self.__balance = self.__balance+amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Invalid amount. Please enter a positive value.")
    
    def withdraw(self, amount):     # setter method to modify the private variable __balance
        if amount > 0 and amount <= self.__balance:
            self.__balance = self.__balance-amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
        elif amount > self.__balance:
            print("Insufficient balance. Please enter a smaller amount.")
        else:
            print("Invalid amount. Please enter a positive value.")

acc = None
while True:
    print("""Please select between 1 to 4 options to proceed
              1. Create a new Account
              2. Check your current Account Details
              3. Deposite Amount
              4. Withdraw Amount
              5. Please enter any other number to exit
              """)
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        name = input("Enter account holder's name: ")
        bal = float(input("Enter initial balance: "))
        acc = BankAccount(name, bal)
        print("Account created successfully.\n")
    elif ch == 2:
        if acc is None:
            print("No account found. Please create an account first.\n")
        else:
            print("Your Account Details are:")
            print(f"Account holder name: {acc.name}")
            print(f"Account Current Balance: {acc.get_balance()}\n")
    elif ch ==3:
        if acc is None:
            print("No account found. Please create an account first.\n")
        else:
            print("Enter the amount to deposit: ")
            amount = float(input())
            acc.deposit(amount)
    elif ch == 4:
        if acc is None:
            print("No account found. Please create an account first.\n")
        else:
            print("Enter the amount to withdraw: ")
            amount = float(input())
            acc.withdraw(amount)
    else:
        print("Thank you for using our services. Have a nice day!")
        break
