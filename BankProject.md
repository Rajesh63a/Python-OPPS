# 🏦 Python OOP – Bank Account Project (Encapsulation)

## Overview

This project is a **menu-driven Bank Account system** built using Python to demonstrate the concept of **Encapsulation** in Object-Oriented Programming (OOP).

The system allows users to:

* Create an account
* Check account details
* Deposit money
* Withdraw money

---

## Concepts Covered

### 1. Encapsulation

Encapsulation means:

> **Hiding data and allowing controlled access using methods**

* The account balance is stored as a **private variable**:

```python
self.__balance
```

* It cannot be accessed directly from outside the class

---

### 2. Private Variables

* `__balance` is a **private attribute**
* Prevents direct modification like:

```python
acc.__balance = -10000   ❌
```

---

### 3. Getter Method

Used to **read private data safely**

```python
def get_balance(self):
    return self.__balance
```

---

### 4. Setter Methods (Controlled Access)

#### Deposit:

* Adds money only if amount is valid

#### Withdraw:

* Allows withdrawal only if:

  * amount > 0
  * sufficient balance available

---

### 5. Input Handling & Flow Control

* Uses a **menu-driven loop**
* Ensures account is created before operations
* Prevents runtime errors using checks (`acc is None`)

---

## Code Implementation

```python id="bank123"
class BankAccount():
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Invalid amount. Please enter a positive value.")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance = self.__balance - amount
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
    
    elif ch == 3:
        if acc is None:
            print("No account found. Please create an account first.\n")
        else:
            amount = float(input("Enter the amount to deposit: "))
            acc.deposit(amount)
    
    elif ch == 4:
        if acc is None:
            print("No account found. Please create an account first.\n")
        else:
            amount = float(input("Enter the amount to withdraw: "))
            acc.withdraw(amount)
    
    else:
        print("Thank you for using our services. Have a nice day!")
        break
```

---

## Sample Flow

```text
1 → Create account  
2 → View account details  
3 → Deposit money  
4 → Withdraw money  
5 → Exit
```

---

## Key Learnings

* Private variables protect sensitive data
* Methods control how data is accessed and modified
* Encapsulation improves:

  * Security 
  * Code maintainability 
  * Data integrity

---

## Possible Enhancements

* Add multiple accounts support
* Implement money transfer between accounts
* Add input validation using `try-except`
* Store data in a file/database

---

## Conclusion

This project demonstrates how **Encapsulation**:

* Prevents direct access to sensitive data
* Ensures safe operations using methods
* Helps build real-world secure systems

---
