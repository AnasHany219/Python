from pydoc import stripid
# ------------------------------------String------------------------------------

# Examples:


myStringOne     = 'This is Single Quote'
myStringTwo     = "This is Double Quotes"
print(myStringOne)
print(myStringTwo)

myStringThree   = 'This is Single Quotes "Test"'
myStringFour    = "This is Double Quotes 'Test'"
print(myStringThree)
print(myStringFour)

myStringFive = '''First
Second    'test' "test"
Third'''
myStringSex = """First
Second    'test' "test"
Third"""
print(myStringFive)
print(myStringSex)

# --------------------------Strings Indexing & Slicing--------------------------

# Indexing "Access Single Item":
myString = "I Love Python"
print(myString[0])      # I -> First Character from left
print(myString[5])      # e -> 5th   Character from left

print(myString[-1])     # n -> First Character from right
print(myString[-5])     # y -> 5th   Character from right

# Slicing "Access Multiple Sequence Items":
# [Start:End] End Not Enclude 
print(myString[7:12])   # Pytho
print(myString[-6:-1])  # Pytho

print(myString[:7])     # I Love -> If start Not written, will start from 0
print(myString[7:])     # Python -> if ent   Not written, will go to end
print(myString[:])      # Full String

# [Start:End:Steps]
print(myString[::])     # I Love Python
print(myString[::1])    # I Love Python
print(myString[::2])    # ILv yhn
print(myString[::3])    # Io tn
print(myString[::4])    # Ivyn

# --------------------------------String Methods--------------------------------
# len()
a = "I Love Python"
print(len(a))   # print the length including the spaces

# lstrip() & strip() & rstrip()
a = "     I Love Python     "
print(a.lstrip())
print(a.strip())
print(a.rstrip())

a = "#####I Love Python#####"
print(a.lstrip("#"))    #I Love Python#####
print(a.strip("#"))     #I Love Python
print(a.rstrip("#"))    ######I Love Python

a = "@@@@@I Love Python#####"
print(a.lstrip("@#"))    #I Love Python#####
print(a.strip("@#"))     #I Love Python
print(a.rstrip("@#"))    #@@@@@I Love Python

# Title()
a = "i love programming"
print(a.title())

# Capitalize()
a = "i love programming"
print(a.capitalize())

# zfill()
a, b, c = "1", "11", "111"
print(a.zfill(3))       # 001
print(b.zfill(3))       # 011
print(c.zfill(3))       # 111

# Upper() & Lower()
a = "AnAs"
print(a.upper())        # ANAS
print(a.lower())        # anas

# split() & rsplit()
a = "I Love C++ and Python and MySQL"
print(a.split())        # ['I', 'Love', 'C++', 'and', 'Python', 'and', 'MySQL']

a = "I-Love-C++-and-Python-and-MySQL"
print(a.split("-"))     # ['I', 'Love', 'C++', 'and', 'Python', 'and', 'MySQL']
print(a.split("-", 2))  # ['I', 'Love', 'C++-and-Python-and-MySQL']
print(a.rsplit("-", 2)) # ['I-Love-C++-and-Python', 'and', 'MySQL']

# Center()
a = "anas"
print(a.center(10))     # Spaces
print(a.center(10, "#"))# Hashes

# Count()
a = "I Love C++ and Python Because they are easy!"
print(a.count("e"))
print(a.count("e", 0, 21))  # char, start, end

# SwapCase()
a = "I Love Python"
b = "i lOVE pYTHON"
print(a.swapcase())     # i lOVE pYTHON -> b
print(b.swapcase())     # I Love Python -> a

# startswith()  & endswith
a = "I Love Python"
print(a.startswith("I"))    # True
print(a.startswith("P"))    # False
print(a.startswith("P", 7)) # True

print(a.endswith("n"))      # True
print(a.endswith("e"))      # False
print(a.endswith("e", 0, 6))# True

# Index(SubString, start, end) & find(SubString, start, end)
a = "I Love Python"
print(a.index("P"))         # 7
print(a.find("P"))          # 7

print(a.index("P", 0, 10))  # 7
print(a.find("P", 0, 10))   # 7

# print(a.index("P", 0 , 5))# ValueError: substring not found
print(a.find("P", 0, 5))    # -1

# ljsut(Width, Fill Char) & rjsut(Width, Fill Char)
a = "Anas"
print(a.ljust(10, "$"))     # Anas$$$$$$
print(a.rjust(10, "$"))     # $$$$$$Anas

# splitlines()
a = '''First Line
Second Line
Third Line'''
b = "First Line\nSecond Line\nThird Line"
print(a.splitlines())       # ['First Line', 'Second Line', 'Third Line']
print(b.splitlines())       # ['First Line', 'Second Line', 'Third Line']

# expandtabs()
a = "Hello,\tPython!\tI\tLove\tC++"
print(a.expandtabs(2))      # Hello,  Python! I Love  C++

# isTitle()
a = "I Love Python"
b = "I love Python"
print(a.istitle())          # True
print(b.istitle())          # False

# isSpace()
a = " "
b = ""
print(a.isspace())          # True
print(b.isspace())          # False

# isUpper() & isLower
a = "I LOVE PYTHON"
b = "i love python"
print(a.isupper())          # Ture
print(b.islower())          # Ture

# isIdentifier()
a = "Anoos"
b = "Anoos_219"
c = "219Anoos"
print(a.isidentifier())     # True
print(b.isidentifier())     # True
print(c.isidentifier())     # False

# isalpha() & isalnum()
a = "AaBbCc"
b = "AaBb12"
c = "123456"
print(a.isalpha())          # True
print(b.isalpha())          # False
print(c.isalpha())          # False

print(a.isalnum())          # True
print(b.isalnum())          # True
print(c.isalnum())          # True

print(a.isdigit())          # False
print(b.isdigit())          # False
print(c.isdigit())          # True

# Replace(Old Value, New Value, Count)
a = "One Two Three One One"
print(a.replace("One", "1", 2))

# join(Itreable)
a = ["Anas", "Hany", "219"]
print('_'.join(a))          # Anas_Hany_219
print(' '.join(a))          # Anas Hany 219

# ------------------------------Strings Formatting----------------------

Name = "Anas"
Age = 21
Rank = 2.97

# print("My Name is " + Name + ",My Age is " + Age + ", My Rank is " + Rank) # TypeError: can only concatenate str (not "int") to str
# %s -> String & %d -> Digit & %f -> float

print("I'm is %s, My Age is %d, My Rank is %.2f." % (Name, Age, Rank))                  # Old Way
print("I'm is {}, My Age is {}, My Rank is {}.".format(Name, Age, Rank))                # New Way
print("I'm is {1}, My Age is {0}, My Rank is {2}.".format(Age, Name, Rank))             # ReArrange Items
print("I'm is {:s}, My Age is {:d}, My Rank is {:f}.".format(Name, Age, Rank))          # New Way
print("I'm is {1:s}, My Age is {0:d}, My Rank is {2:f}.".format(Age, Name, Rank))       # ReArrange Items

print("I'm is {Name}, My Age is {Age}, My Rank is {Rank}.")     # I'm is {Name}, My Age is {Age}, My Rank is {Rank}.
print(f"I'm is {Name}, My Age is {Age}, My Rank is {Rank}.")    # I'm is Anas, My Age is 21, My Rank is 2.97.

#Format Money
money = 100000000
print("His Money is {:,d}".format(money))