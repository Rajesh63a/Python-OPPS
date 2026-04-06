# 🐶 Python OOP – Inheritance & Method Overriding

## Overview

This project demonstrates **Object-Oriented Programming (OOP)** concepts in Python, specifically:

* Inheritance
* Method Overriding
* Using `super()`

We extend a base `Animal` class into a specialized `Dog` class.

---

## Concepts Covered

### 1. Inheritance

* A child class (**Dog**) inherits properties and methods from a parent class (**Animal**)
* Promotes **code reuse** and avoids duplication

👉 Example:
Dog **IS A** Animal

---

### 2. Method Overriding

* A child class can **override** a method from the parent class
* Allows customizing behavior

---

### 3. `super()`

* Used to call the **parent class method**
* Helps extend functionality instead of completely replacing it

---

## Code Implementation

```python
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Hi, My name is {self.name} and I'm {self.age} years old.")

class Dog(Animal):
    def introduce(self):
        super().introduce()
        print("I'm a dog.")
    
    def bark(self):
        print(f"{self.name} is barking: Woof!")

dog = Dog("Buddy", 3)

dog.introduce()
dog.bark()
```

---

## Sample Output

```
Hi, My name is Buddy and I'm 3 years old.
I'm a dog.
Buddy is barking: Woof!
```

---

## Key Learnings

* Child classes inherit **attributes and methods** from parent classes
* Method overriding allows **custom behavior** in child classes
* `super()` enables calling parent methods inside child class
* Helps build **clean, reusable, and scalable code**

---

## Structure

```
Animal (Parent Class)
 ├── name
 ├── age
 └── introduce()

Dog (Child Class)
 ├── inherits all from Animal
 ├── overrides introduce()
 └── adds bark()
```
---

## Conclusion

This project demonstrates how inheritance and method overriding:

* Reduce code duplication
* Improve structure
* Make programs more flexible

---

