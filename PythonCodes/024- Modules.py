# ------------------------------------------- Modules -------------------------------------------
# [1] Module is a file contain a set of function
# [2] Module save your time
# [3] You can import module in your app to help you
# [4] You can import Multiple modules
# [5] You can create your own module

# Import main module
import random
print(f"Printing a random number: {random.random()}")

# Show all function inside module
print(dir(random))

# import one or two functions from module
from random import randint
print(f"Printing random interger form 10 to 15: {randint(10, 15)}")

# --------------------------------------- Create Modules ----------------------------------------
import NewModule
# def sayHello(name):
#     print(f"Hello, {name}!")
# def sayHowAreYou(name):
#     print(f"How Are You, {name}?")

print(dir(NewModule))                   # ['sayHello', 'sayHowAreYou']
NewModule.sayHello("Anas")              # Hello, Anas!
NewModule.sayHowAreYou("Anas")          # How Are You, Anas?

# ---------------------------------- Install External Packages ----------------------------------
# [1] Modules vs Packages
# [2] External packages downloaded from the internet 
# [3] You can install package from python package manager PIP
# [4] PIP install the package and its dependencies
# [5] Modules list "https://docs.python.org/3/py-modindex.html"
# [6] Package and modules directory "https://pypi.org/"
# [7] PIP manual "https://pip.pypa.io/en/stable/reference/pip_install/"
