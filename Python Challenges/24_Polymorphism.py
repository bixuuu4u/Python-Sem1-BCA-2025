# Demonstration of Static and Dynamic Polymorphism in Python

# Dynamic Polymorphism (Method Overriding)

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Creating objects
animal = Animal()
dog = Dog()
cat = Cat()

animal.speak()  # Calls parent class method
dog.speak()     # Calls Dog's overridden method
cat.speak()     # Calls Cat's overridden method
