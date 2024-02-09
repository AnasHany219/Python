# ----------------------- DocStrings and Commenting vs Documenting ----------------------- 
# [1] Documentation string for Class, Module or Function
# [2] Can be accessed from the help() or Doc attributes
# [3] Made for understanding the functionality of complex code
# [4] There's one line and multiple lines Doc strings

def fun(name):
    '''This is funciton to say hello''' # multi lines by """ * """
    print(f"Hello, {name}!")

print(fun.__doc__)                      # This is funciton to say hello
fun("Anas")                             # Hello, Anas!
help(fun)                               # fun(name) - This is funciton to say hello
