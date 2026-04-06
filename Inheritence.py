#parent class
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Hi, My name is {self.name} and I'm {self.age} years old.")

#Dog class inherits from Animal class
class Dog(Animal):
    def introduce(self):     #Override the introduce method of the parent class
        super().introduce()  # Call the introduce method of the parent class (Animal)
        print("I'm a dog.")
    def bark(self):
        print(f"{self.name} is barking: Woof!")

dog = Dog("Buddy", 3)
dog.introduce()
dog.bark()
