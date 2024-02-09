# -------------------------------- Decorator -------------------------------- 
# [1] Sometime called meta programming
# [2] Every thing in python is object even function
# [3] Decorator take a function and add some functionality and return it
# [4] Decorator warp other funciton and enhance their behaviour
# [5] Decorator is higher order function (Function Accept function as parameter)

def fun():
    print("During Function")

def dec(fun):
    def nested_fun():
        print("Befor function")
        fun()
        print("After function")
    return nested_fun 

dec(fun)()                              # Befor function - During Function - After function