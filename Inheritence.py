#parent class
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Hi, My name is {self.name} and I'm {self.age} years old.")

#Dog class inherits from Animal class
class Dog(Animal):
    def __init__(self, name, age, behavior):     # This is constructor overloading, we are defining a new constructor for the Dog class which is different from the constructor of the Animal class
        super().__init__(name, age)              # Call the constructor of the parent class (Animal) to initialize the name and age attributes. This ia an example of constructor chaining, where the constructor of the child class calls the constructor of the parent class to initialize the inherited attributes.
        self.behavior = behavior
    def introduce(self):                         #Override the introduce method of the parent class
        super().introduce()                      # Call the introduce method of the parent class (Animal)
        print("I'm a dog.")
    def bark(self):
        print(f"{self.name} is barking: Woof! and behavior is {self.behavior}")

dog = Dog("Buddy", 3, "Friendly")
dog.introduce()
dog.bark()
