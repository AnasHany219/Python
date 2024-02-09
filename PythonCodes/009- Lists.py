# ------------------------- Lists -------------------------
# [1] List Items are Enclosed in Square Bracktes
# [2] List are Ordered, To use index to access bracktes
# [3] List are Mutable -> Add, Delete, Edit
# [4] List Items are Not unique
# [5] List can have different data type

MyList = [1, 3, 1, "One", "Two", 1.1, True]

print(MyList)           # [1, 3, 1, 'One', 'Two', 1.1, True]

print(MyList[0])        # 1
print(MyList[2])        # 1

print(MyList[-1])       # True
print(MyList[-3])       # Two 

print(MyList[:3])       # [1, 3, 1]
print(MyList[3:5])      # ['One', 'Two']
print(MyList[5:])       # [1.1, True]

print(MyList[::2])      # [1, 1, 'Two', True]

# Edit
MyList[0:2] = ['One', 'Two']
MyList[2] = "One"
MyList[3:5] = [1, 2]
MyList[5:] = [2.2, False]
print(MyList)           # ['One', 'Two', 'One', 1, 2, 2.2, False]

# Delete
MyList[0:2] = [1]
MyList[1:3] = []
print(MyList)           # [1, 2, 2.2, False]

# --------------------- Lists Methods ---------------------
# append() -> adding elements to the end of the list
myNumbers = ["One", 2, "Three"]
myNumbers.append(4)
myNumbers.append("Five")
myNumbers.append(False)
print(myNumbers)        # ['One', 2, 'Three', 4, 'Five', False]

# extend() -> marge lists
a = ["one", "two", "three"]
b = [4, 5, 6]
a.extend(b)
print(a)                # ['one', 'two', 'three', 4, 5, 6]

# remove() -> delete an element
a = ["one", "two", "three", "three", 4, 5, 6]
a.remove("three")
print(a)                # ['one', 'two', 'three', 4, 5, 6]

# sort()
a = [2, 3, 1, 5, 4]
a.sort(reverse = True)  # [5, 4, 3, 2, 1]
a.sort(reverse = False) # [1, 2, 3, 4, 5]
print(a)

# reverse
a = [2, 3, 1, 5, 4]
a.reverse()
print(a)                # [4, 5, 1, 3, 2]

# clear()
a = [2, 3, 1, 5, 4]
a.clear()
print(a)                # []

# copy()
a = [2, 3, 1, 5, 4]
b = a.copy()            # b = a
print(b)                # [2, 3, 1, 5, 4]

# count()
a = [1, 2, 1, 3, 1, 5, 1, 4, 1]
print(a.count(1))       # 5

# index()
a = [0, 1, 2, 3, 4, 5, 6]
print(a.index(6))       # 6

# insert()
a = [0 ,1, 2, 4, 5, 7]
a.insert(3, "Three")
a.insert(-1, "Sex")
print(a)                # [0, 1, 2, 'Three', 4, 5, 'Sex', 7]

# pop()
a = [0, 1, 2, 'Three', 4, 5, 'Sex', 7]
print(a.pop())          # 7
print(a)                # [0, 1, 2, 'Three', 4, 5, 'Sex']