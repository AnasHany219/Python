# ----------------------------- Tuple ----------------------------- 
# [1] Tuple Items R enclosed in Parantheses ()
tuple1 = ("anas", "hany")
print(type(tuple1))             # <class 'tuple'>

# [2] U can remove the paranthese if U want
tuple1 = "anas", "hany"
print(type(tuple1))             # <class 'tuple'>

# [3] Tuple are ordered, To use indexing to access an item
tuple1 = (0, 1, 2, 3, 4, 5)
print(tuple1[3])                # 3
print(tuple1[-3])               # -3

# [4] Tuple are immutable, You can add or delete
tuple1 = (0, 1, 2, 3, 4, 5) 
# tuple1[3] = "three"           # TypeError: 'tuple' object does not support item assignment

# [5] Tuple items are not unique
tuple1 = (0, 1, 2, 1, 4, 1) 
print(tuple1)                   # (0, 1, 2, 1, 4, 1)

# [6] Tuple can have different data types 
tuple1 = (False, True, 2, "Three", 4.5)
print(tuple1)                   # (False, True, 2, 'Three', 4.5)

# [7] Operators Usend in Strings and Lists are available in Tuples
# -----------------------------------------------------------------
# Tuple with one element
tuple1 = ("Anas")
tuple2 = ("Anas",)

print(tuple1)                   # Anas
print(tuple2)                   # ('Anas',)

print(type(tuple1))             # <class 'str'>
print(type(tuple2))             # <class 'tuple'>

# Tuple Concatenation
tuple1 = (0, 1, 2)
tuple2 = (3, 4, 5)

tuple1 += tuple2
print(tuple1)                   # (0, 1, 2, 3, 4, 5)

# Tuple, List, and String repeat(*)
myString = "One"
print(myString * 3)             # OneOneOne

myList = [1, 2] 
print(myList * 3)               # [1, 2, 1, 2, 1, 2]

myTuple = (1, 2)
print(myTuple * 3)              # (1, 2, 1, 2, 1, 2)

# ---------------------------- Methods ----------------------------
# Count()
tuple1 = (0, 1, 2, 1, 4, 1) 
print(tuple1.count(1))          # 3

# Index()
tuple1 = (0, 1, 2, 3, 4, 5)
print(tuple1.index(3))          # 3 -> position

# Tuple destruct
tuple1 = ("A", "B", 3, "C")
a, b, _,c = tuple1
print(a)                        # A
print(b)                        # B
print(c)                        # C