# ------------------------------- Iterable vs Iterator -------------------------------
# Iterable
# [1] Object contains data that can be iterated upon
# [2] Examples:- String, list, set, tuple, dictionary

s = "Iterable"
for l in s:
    print(l, end=" ")                   # I t e r a b l e 
print()

# Iterator
# [1] Object use to iterate over the iterable using next() method that return 1 element at a time
# [2] You can generate iterator from iterable when using iter() method
# [3] For loop already call iter() method on the iterable behind the scene
# [4] Gives "StopIteration" if there is no next element

s = "Iterator"
it = iter(s)
print(next(it))                         # I
print(next(it))                         # t
print(next(it))                         # e
print(next(it))                         # r
print(next(it))                         # a
print(next(it))                         # t
print(next(it))                         # o
print(next(it))                         # r