# ----------------------------- Built In Functions ----------------------------- 

# All()                         -> If all elements in the list are ture? return true
x = [1, 2, 3]
if all(x):  print("All Elements are ture.")
else:       print("There is at leas 1 element is false")

# Any()                         -> If 1 element in the list is ture? return true
x = [1, 0, []]
if any(x):  print("There is at leas 1 element is true")
else:       print("All Elements are false.")

# Bin()                         -> Convert decimal to binary
print(bin(10))                  # 0b1010

# Id()                          -> There is and id for all variables
a = 1
b = 2
print(id(a))                    # 140723559254456
print(id(b))                    # 140723559254488

# sum(iterable, start)
a = [1, 2, 3, 4, 5]
print(sum(a))                   # 15
print(sum(a, 5))                # 20
print(sum(a, 10))               # 25

# round(number, number of digits)
print(round(100.499))           # 100
print(round(100.500))           # 100
print(round(100.501))           # 101
print(round(100.505, 2))        # 100.5
print(round(100.555, 2))        # 100.56

# range(start, end, step)
print(list(range(10)))          # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(5, 10)))       # [5, 6, 7, 8, 9]
print(list(range(0, 10, 2)))    # [0, 2, 4, 6, 8]

# print()
print("Hello Anas! How are you?")                           # Hello Anas! How are you?
print("Hello", "Anas!", "How", "are", "you?")               # Hello Anas! How are you?
print("Hello", "Anas!", "How", "are", "you?", sep = "-")    # Hello-Anas!-How-are-you?

print("First Line", end = " ")  
print("Second Line")            # First Line Second Line
print("Third Line")             # Third Line

# abs()
print(abs(-10))                 # 10
print(abs(10))                  # 10

# pow(base, exp, mod)
print(pow(2, 5))                # 32
print(pow(2, 5, 10))            # 32 % 10 = 2

# min(item, item, item, or iterator)
print(min('A', 'a', "S", "X"))  # A
print(min(5, 3, 1, 2))          # 1
a = range(6, 10)
print(min(a))                   # 6

# max(item, item, item, or iterator)
print(max('A', 'a', "S", "X"))  # a
print(max(5, 3, 1, 2))          # 5
a = range(6, 10)
print(max(a))                   # 9

# slice(start, end, step)
a = ["A", "B", "C", "D", "E"]
print(a[:])                     # ['A', 'B', 'C', 'D', 'E']
print(a[:4])                    # ['A', 'B', 'C', 'D']
print(a[slice(4)])              # ['A', 'B', 'C', 'D']
print(a[2:4])                   # ['C', 'D']
print(a[slice(2, 4)])           # ['C', 'D']
print(a[slice(2, 4, 2)])        # ['C']

# enumerate(iterator, start = 0)
lang = ["C++", "HTML", "CSS", "Java", "Python"]
langs = enumerate(lang, 1)
print(type(langs))              # <class 'enumerate'>

for l in lang:
    print(l, end = " - ")       # C++ - HTML - CSS - Java - Python -
print()

for c, l in langs:
    print(f"{c}, {l} -", end = " ")       # 1, C++ - 2, HTML - 3, CSS - 4, Java - 5, Python -
print()

# help
# print(help(print))

# reversed()
s = "912_sanA"
print(reversed(s))              # <reversed object at 0x000001F5F00B89D0>
for c in reversed(s):
    print(c, end="")            # Anas_219
print()

# ------------------------------------ Map ------------------------------------ 
# [1] Map take a function + Iterator
# [2] Map Called up map because It map the function on every element
# [3] The Function can be pre-defined function or lambda function

my_texs = ["Anas", "Islam", "Amjad"]

# Use map with pre-defined function
def format_text(text):
    return f"- {text} -"

map_text = map(format_text, my_texs)

for text in map_text:
    print(text, end='')         # - Anas -- Islam -- Amjad -
print()

# Use map with lambda function
for text in list(map(lambda text : f"- {text} -", my_texs)):
    print(text, end='')         # - Anas -- Islam -- Amjad -
print()

# ---------------------------------- Filter ----------------------------------- 
# [1] Filter take a function + iterator
# [2] Filter run  a function on every element
# [3] Filter out all elements for which the function return true
# [4] The Function can be pre-defined function or lambda function
# [5] The Function need to return boolean value

a = [10, 5, 9, 13, 8, 15, 3, 2]

# Use filter with pre-defined function
def checkNumber(num):
    if num < 10:
        return num

res = filter(checkNumber, a)

for i in res:
    print(i, end=' ')           # 5 9 8 3 2
print()

# Use filter with lambda function
for i in list(filter(lambda num : num < 10, a)):
    print(i, end=' ')           # 5 9 8 3 2
print()

# ---------------------------------- Reduce ----------------------------------- 
# [1] Reduce take a function + iterator
# [2] Reduce run  a funciton on the first and second element and give result
# [3] Then   run  a function on result    and third  element
# [4] Then   run  a function on result    and fourth element and so on
# [5] Till one element is left and this is the result of the reduce
# [6] The Function can be pre-defined function or lambda function

from functools import reduce

nums = [1, 2, 3, 4, 5]
def sumAll(num1, num2):
    return num1 + num2

res1 = reduce(sumAll, nums, 15)
print(res1)                   # 30

res2 = reduce(lambda num1, num2: num1 + num2, nums, 15)
print(res2)                   # 30

print(sum(nums) + 15)           # 30