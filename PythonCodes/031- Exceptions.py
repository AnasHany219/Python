# ---------------------------------- Exceptions ----------------------------------
# [1] Exception is a runtime error reproting mechanism
# [2] Exception give you a message to understand the problem
# [5] Trackback give you the line to look for the code in this line 
# [3] Exception types:- [SyntaxError, IndexError, KeyError, etc ...]
# [4] Exception list :- https://docs.python.org/3/library/exceptions.html
# [6] raise keyword used to raise your own exception

x = 10
if(x < 0):  print("Only Positive numbers")
else:       print("200 OK!")                            # 200 OK!
print("Done!")                                          # Done!

# x = -10
# if(x < 0):  raise Exception("Only Positive numbers")    # Only Positive numbers
# else:       print("200 OK!")
# print("Done!")

# ----------------------------- Exceptions Handling ------------------------------
# ------------------------ Try | Except | Else | Finally -------------------------
# Try       -> Test the code errors
# Except    -> Handle the error
# Finally   -> Run The code
# Else      -> If no Error

try:
    age = int(input("Enter your age: "))
except:
    print("Only Enter an integer number")
else:
    print(f"Your age is: {age}")
finally:
    print("Done!")