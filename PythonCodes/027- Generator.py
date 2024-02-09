# ------------------------------- Generator -------------------------------
# [1] Generator is a function with "yield" keyword Instead of "return"
# [2] Its support iteration and retern generator iterator by calling "yield"
# [3] Generator function can have one or more "yield"
# [4] By using next() it resume from where it called "yield" not from begining
# [5] When called, its not start automatically, its give you the control

def gen():
    yield "Hello,"
    yield "How"
    yield "You?"
Generator = gen()
print(next(Generator))                  # Hello,
print("Anas!")                          # Anas!
print(next(Generator))                  # How
print("Are")                            # Are
print(next(Generator))                  # You?

