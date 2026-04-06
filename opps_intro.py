from BankProject import BankAccount

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

