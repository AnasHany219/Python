# -------------------- Type Conversion -------------------- 

# str()
a = 10
print(type(a))                  # <class 'int'>
print(type(str(a)))             # <class 'str'>

# tuple()
a = "anas"                      # string
print(tuple(a))                 # ('a', 'n', 'a', 's')
b = [1, 2, 3]                   # list
print(tuple(b))                 # (1, 2, 3)
c = {'a', 'b', 'c'}             # set
print(tuple(c))                 # ('c', 'b', 'a')
d = {'a' : 1, 'b' : 2}          # dictionary
print(tuple(d))                 # ('a', 'b')

# list()
a = "anas"                      # string
print(list(a))                  # ['a', 'n', 'a', 's']
b = (1, 2, 3)                   # tuple
print(list(b))                  # [1, 2, 3]
c = {'a', 'b', 'c'}             # set
print(list(c))                  # ['c', 'b', 'a']
d = {'a' : 1, 'b' : 2}          # dictionary
print(list(d))                  # ['a', 'b']

# set()
a = "anas"                      # string
print(set(a))                   # {'s', 'a', 'n'}
b = [1, 2, 3]                   # list
print(set(b))                   # {1, 2, 3}
c = ('a', 'b', 'c')             # tuple
print(set(c))                   # {'a', 'c', 'b'}
d = {'a' : 1, 'b' : 2}          # dictionary
print(set(d))                   # {'a', 'b'}

# set()
c = (('a', 1), ('b', 2))        # tuple
print(dict(c))                  # {'a': 1, 'b': 2}
b = [['a', 1], ['b', 2]]        # list
print(dict(b))                  # {'a': 1, 'b': 2}