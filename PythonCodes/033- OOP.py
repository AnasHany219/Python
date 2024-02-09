# -------------------------------------- Object Oriented Programming --------------------------------------
# ------------------------------------- Class Syntax and information --------------------------------------
# [01] Class is blueprint or constructor of the Object
# [02] Class instantiate mean ceate an instance of the class
# [03] Instance -> object created from the classes and have their methods and Attributes
# [04] Class defined with keyword 'class'
# [05] Class name written with PascalCass 'UpperCamelCass' Style
# [06] Class may contain methods and attributes
# [07] When creating object python look for the built in __init__ method
# [08] __init__ Method called every time you create object from class
# [09] __init__ is the initialize the date for the object
# [10] Any method with two underscore in the start and the end is called 'Dunder' or 'Magic' Method
# [11] self refer to the current instance created form the class and must be first parameter
# [12] self can be named anything
# [13] In the python, you don't need to call new() keyword to create Object

class Member:
    def __init__(self):
        print("New member has been added!")
Member()                                    # New member has been added!
Member()                                    # New member has been added!
m1 = Member()                               # New member has been added!
print(m1.__class__)                         # <class '__main__.Member'>

# ------------------------------------- Instance attribute and method --------------------------------------
# self                  -> Point to instance created from class
# Instance Method       -> Take self parameter which point to instance created from class 
# Instance Method       -> Can have more one parameter like any function
# Instance Method       -> Can access the class itself
# Instance Method       -> Can freely access attributes and method in the same object
# Instance attribute    -> Definde inside the constructor

class Member:
    UserNumber = 0
    def __init__(self, name, age, gender):
        self.age = age
        self.name = name
        self.gender = gender
        Member.UserNumber += 1

    def display(self):
        if self.gender == "Male":
            print(f"Hello Mr {self.name}, Your Age: {self.age}")
        elif self.gender == "Female":
            print(f"Hello Miss {self.name}, Your Age: {self.age}")
        else:
            print(f"Hello {self.name}, Your Age: {self.age}")

    def UsersNumber(self):
        print(f"Numebr of Users = {Member.UserNumber}")
m1 = Member("Anas", "20", "Male") 
m2 = Member("Islam", "21", "Male") 
m3 = Member("Amjad", "22", "Male") 

print(m1.age)                               # 20
print(m1.name)                              # Anas
m1.display()                                # Hello Mr Anas, Your Age: 20
m1.UsersNumber()                            # Numebr of Users = 3

# ------------------------------------- Class method and Static method -------------------------------------
# Class Method  -> Marked with @classmethod Decorator to flag it as class method
#               -> It take 'Cls' parameter not 'self' to point to the class not the instance
#               -> It doesn't require a creation of a class instance
#               -> Used when you want to do something with the class itself
# Static Method -> It take no parameters
#               -> It bounds to the class not instance
#               -> Used when doing something doesn't have access to object or class but related to the class
class Member:
    UserNumber = 0
    def __init__(self, name):
        self.name = name
        Member.UserNumber += 1

    @classmethod
    def UsersNumber(cls):
        print(f"We have {cls.UserNumber} Users in our system")
    
    @staticmethod
    def hello():
        print("Hello, dude!")
    
    def display(self):
        print (f"Hello, {self.name}!")

m1 = Member("Anas")
m1.hello()                                  # Hello, dude!
m1.display()                                # Hello, Anas!
m1.UsersNumber()                            # We have 1 Users in our system

# ---------------------------------------------- Inheritance -----------------------------------------------
class Food:
    def __init__(self, name) -> None:
        self.name = name
        print(f"{self.name} Class has been created - Base Class.")
    def eat(self):
        print("Eat Method - Base Class")

class Apple(Food):
    def __init__(self, name) -> None:
        super().__init__(name)
        print(f"{self.name} Class has been Created - Derived Class.")

a = Apple("Pizza")
a.eat()                                     # Pizza Class has been Created - Base Class.
                                            # Pizza Class has been Created - Derived Class.
                                            # Eat Method - Base Class

