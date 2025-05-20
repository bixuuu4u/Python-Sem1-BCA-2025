# Object-Oriented Programming (OOP) is a programming style
# that organizes code into objects. It helps in making code reusable, modular, and easy to understand.


# class = A blueprint/template for creating objects.
# object= An instance of a class (real-world entity).
#  Class---is a blank form if it is filled with peritacular information it is object
# Attribute = Variables that belong to an object (data).
# Methods =	Functions inside a class that define behaviors.

class Employee:
    # Class attribute
    language ="Python"  #All employees language is python

    def getInfo(self):
        print(f"The language is {self.language}")


#if self is not given e1.getInfo()  ->> Employee.getInfo(e1) here one arugemnt is passed but no was given


e1=Employee()
e1.language="java"  #Instance attribute MORE PRIORITY
e1.getInfo()