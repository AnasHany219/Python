# ---------------------------------------- Set ----------------------------------------
# Set items are enclosed in curly braces
set1 = {0, 1, 2, 3, 4, 5}

# Set items are not ordered and not indexed
set1 = {"Anas", "Hany", 219}    
print(set1)                     # {'Anas', 219, 'Hany'} or another
# print(set1[0])                # TypeError: 'set' object is not subscriptable

# Set indexing and slicing cannot be done
tuple1  = (0, 1, 2, 3, 4, 5)
set1    = {0, 1, 2, 3, 4, 5}

print(tuple1[0:3])              # (0, 1, 2)
# print(set1[0:3])              # TypeError: 'set' object is not subscriptable

# Set has only immutable data types (Number, String, Tuples), List and dict are not
# set1 = {"Anas", "Hany", 219, 9.3, True, [1, 2, 3]}    # TypeError: unhashable type: 'list'

set1 = {"Anas", "Hany", 219, 9.3, True, (1, 2, 3)}
print(set1)                     # {True, 'Hany', 'Anas', 9.3, (1, 2, 3), 219}

# Set items are unique
set1 = {1 , 2, 1, 3, 2, 4, 3, 1}
print(set1)                     # {1, 2, 3, 4}

# ------------------------------------ Set Methods ------------------------------------
# Clear()
a = {1, 2, 3}
a.clear()
print(a)                        # set()

# Union
a = {1, 2, 3}
b = {"One", "Two", "Three"}
a = a.union(b)                  # a |= b
print(a)                        # {1, 2, 3, 'Three', 'One', 'Two'}

# Add()
a = {1, 2, 3}
# a.add(5, 6)                   # TypeError: set.add() takes exactly one argument (2 given)
a.add(5)
a.add(6)
print(a)                        # {1, 2, 3, 5, 6}

# Copy()
a = {1, 2, 3}
b = a.copy()
print(a)                        # {1, 2, 3}
print(b)                        # {1, 2, 3}

# Remove()
a = {1, 2, 3, 4}
# a.remove(9)                   # KeyError: 9
a.remove(1)
print(a)                        # {2, 3, 4}

# Discard()
a = {1, 2, 3, 4}
a.discard(9)                   
a.discard(1)
print(a)                        # {2, 3, 4}

# Pop()
a = {"Anas", "Hany", 219, 9.3, True, (1, 2, 3)}
print(a.pop())                  # True  -> random item

# Update()
a = {1, 2, 3}
b = {"One", "Two", "Three"}
print(a)                        # {1, 2, 3}
print(b)                        # {'Three', 'Two', 'One'}
a.update(b)                     # U can add list
print(a)                        # {1, 2, 3, 'One', 'Three', 'Two'}
print(b)                        # {'Three', 'Two', 'One'}

# -------------------------------------------------------------------------------------
# Difference
a = {1, 2, 3, 4}
b = {1, 2, "3", "4"}
print(a)                        # {1, 2, 3, 4}
print(a.difference(b))          # {3, 4}
print(a - b)                    # {3, 4}
print(a)                        # {1, 2, 3, 4}

# Difference_Update
a = {1, 2, 3, 4}
b = {1, 2, "3", "4"}
print(a)                        # {1, 2, 3, 4}
a.difference_update(b)          # a -= b
print(a)                        # {3, 4}

# Intersection()
a = {1, 2, 3, 4}
b = {1, 2, "3", "4"}
print(a)                        # {1, 2, 3, 4}
print(a.intersection(b))        # {1, 2}
print(a & b)                    # {1, 2}
print(a)                        # {1, 2, 3, 4}

# Intersection_Update()
a = {1, 2, 3, 4}
b = {1, 2, "3", "4"}
print(a)                        # {1, 2, 3, 4}
a.intersection_update(b)        # a &= b
print(a)                        # {1, 2}

# Symmetric_Difference()
a = {1, 2, 3, 4}
b = {1, 2, "3", "4"}
print(a)                            # {1, 2, 3, 4}
print(a.symmetric_difference(b))    # {'3', 3, 4, '4'}
print(a ^ b)                        # {'3', 3, 4, '4'}
print(a)                            # {1, 2, 3, 4}

# Symmetric_Difference()
a = {1, 2, 3, 4}
b = {1, 2, "3", "4"}
print(a)                            # {1, 2, 3, 4}
a.symmetric_difference_update(b)    # a ^ b
print(a)                            # {'4', '3', 3, 4}

# -------------------------------------------------------------------------------------
# isSuperSet()
a = {1, 2, 3, 4}
b = {1, 2, 3}
print(a.issuperset(b))              # True
print(b.issuperset(a))              # False

# isSubSet()
a = {1, 2, 3, 4}
b = {1, 2, 3}
print(a.issubset(b))                # False
print(b.issubset(a))                # True

# isDisJoint()
a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {4, 5, 6}
print(a.isdisjoint(b))              # False
print(b.isdisjoint(c))              # True  