# ---------------------------------------- Function ----------------------------------------
# [1] A Function is a reusable block fo code do a task 
# [2] A Function is for all team and all apps
# [3] A Function run when U call it
# [4] A Function can do the task without returning data
# [5] A Function can return data after the job is Finished
# [6] A Function accept element to deal with [Parameters]
# [7] A Function accept element when u call it [Arguments]
# [8] A Function create to prevent DRY [Don't repeat yourself]
# [9] There's a built-in function and User Defined Funcions

# ----------------------------------- Function and return ----------------------------------
def function(): print("Hello, World!")
function()                              # Hello, World!

def function(): return "Hello, World!"
print(function())                       # Hello, World!

# -------------------------------- Parameters and Arguments --------------------------------
s = "Anas"
def function(name) : print(f"Hello, {name}!")
function(s)                             # Hello, Anas!

# ------------------------- Packing and UnPacking Arguments *Args --------------------------
people = ["Anas", "Islam", "Amjad"]

print(people)                           # ['Anas', 'Islam', 'Amjad']
print(*people)                          # Anas Islam Amjad

def function(*people) :
    for name in people :
        print(f"Hello, {name}!")

function("Anas", "Islam", "Amjad")

# ----------------------------------- Default Parameters -----------------------------------
def function(name = "Unknown", age = "Unknown", country = "Unknown"):
    print(f"Hello, {name}! Your age is {age}. Your country is {country}")   # Hello, anas! Your age is Unknown. Your country is Unknown
function("anas")

# ------------------------------------------ Scope -----------------------------------------
x = "Global"

def function_1(): 
    x = "Function"
    print(f"Print variable from {x}")

def function_2(): 
    global x 
    x = "Function"
    print(f"Print variable from {x}")

print(f"Print variable from {x}")       # Print variable from Global
function_1()                            # Print variable from Function
print(f"Print variable from {x}")       # Print variable from Global
function_2()                            # Print variable from Function
print(f"Print variable from {x}")       # Print variable from Function

# ---------------------------------------- Recursion ---------------------------------------
s = "WWWOOORRRLLLDDD"
def clean(word):
    if len(word) == 1:
        return word
    elif word[0] == word[1]:
        return clean(word[1:])
    else:
        return word[0] + clean(word[1:])

print(clean(s))                         # WORLD

# ----------------------------------------- Lambda -----------------------------------------
# Anonymous function
# [1] It has no name
# [2] You can call it inline without defining it
# [3] You can use it in return data from another function
# [4] Lambda used for simple function and Def handle the large tasks
# [5] Lambda is one single expression not block of code
# [6] Lambda type is function

def hello_fun(name) : return f"Hello, {name}!"   # -> one line function
hello_lambda = lambda name : f"Hello, {name}!"   # -> Lambda   function

print(hello_fun("Anas"))                # Hello, Anas!
print(hello_lambda("Anas"))             # Hello, Anas!