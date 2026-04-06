# 🐶 Python OOP Basics – Dog Intro Project

##  Overview

This project demonstrates the fundamentals of **Object-Oriented Programming (OOP)** in Python using a simple **Dog Intro system**.

We created a `Dog` class with attributes and methods, then instantiated multiple objects and interacted with them.

---

##  Concepts Covered

###  1. Class

A class is a **blueprint** that defines what properties (data) and behaviors (methods) an object should have.

---

###  2. Object

An object is a **real instance of a class** that contains actual data and can perform actions.

---

###  3. Attributes (Data)

Attributes represent **what an object has**.

Example:

* `name`
* `age`

---

###  4. Methods (Behavior)

Methods represent **what an object can do**.

Example:

* `introduce()`
* `bark()`
* `is_puppy()`

---

### 5. Constructor (`__init__`)

* A special method that is called **automatically when an object is created**
* Used to initialize object data

---

### 6. `self`

* Refers to the **current object**
* Used to access attributes and methods inside the class

---

### 7. Encapsulation (Basic)

* Keeping data and related behavior **inside the class**
* Example: `is_puppy()` logic is inside the class

---

## Code Implementation

```python
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Hi, My name is {self.name} and I'm {self.age} years old.")
    
    def bark(self):
        print(f"{self.name} says Woof!")
    
    def is_puppy(self):
        if self.age < 7:
            return True
        else:
            return False

dogs = [Dog("harry", 7), Dog("scooby", 5), Dog("buddy", 3)]

for dog in dogs:
    dog.introduce()
    dog.bark()
    
    if dog.is_puppy():
        print(f"{dog.name} is a puppy.\n")
    else:
        print(f"{dog.name} is not a puppy.\n")
```

---

## Sample Output

```
Hi, My name is harry and I'm 7 years old.
harry says Woof!
harry is not a puppy.

Hi, My name is scooby and I'm 5 years old.
scooby says Woof!
scooby is a puppy.

Hi, My name is buddy and I'm 3 years old.
buddy says Woof!
buddy is a puppy.
```

---

## Key Learnings

* A **class defines structure**, objects hold real data
* Each object has its **own independent values**
* Methods can use object data via `self`
* Logic should be placed **inside the class (OOP principle)**
* Returning values (`True/False`) makes code reusable

---
