# --------------- Numbers --------------- 
# Integers
print(type(100))            # <class 'int'>
print(type(10))             # <class 'int'>
print(type(0))              # <class 'int'>
print(type(-10))            # <class 'int'>
print(type(-100))           # <class 'int'>

# Float
print(type(1.9))            # <class 'float'>
print(type(0.9))            # <class 'float'>
print(type(0))              # <class 'int'>
print(type(-0.9))           # <class 'float'>
print(type(-1.9))           # <class 'float'>

# Complex
ComplexNumber = 21 + 9j
print(type(ComplexNumber))  # <class 'complex'>
print("My Real Part is {}, and My Imaginary Part is {}.".format(ComplexNumber.real, ComplexNumber.imag))

# [1] U Can Convert a Number From Int to Float or Complex
print(type(100))            # <class 'int'>
print(type(float(100)))     # <class 'float'>
print(type(complex(100)))   # <class 'complex'>

# [2] U Can Convert a Number From Float to Int or Complex
print(type(21.9))           # <class 'float'>
print(type(int(21.9)))      # <class 'int'>
print(type(complex(21.9)))  # <class 'complex'>

# [3] U Cannot Convert a Number From Complex to Any Type