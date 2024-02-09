# ------------------------------- Operators -------------------------------
# --------------------------- Boolean Operators ---------------------------
# and
age = 20
country = "Egypt"
print(age > 16 and country == "Egypt")      # True
print(age < 16 and country == "Egypt")      # False

# or
age = 20
country = "Egypt"
print(age > 16 or country == "Egypt")       # True
print(age < 16 or country == "Egypt")       # True

# not
age = 20
country = "Egypt"
print(not age > 16)                         # False
print(not age < 16)                         # True

# ------------------------- Assignments Operators -------------------------
# varOne = varOne [Operator] varTwo -> varOne [Operator]= varTwo

# +=
x, y = 10, 5
x += y
print(x)            # 15

# -=
x, y = 10, 5
x -= y
print(x)            # 5

# *=
x, y = 10, 5
x *= y
print(x)            # 50

# /=
x, y = 10, 5
x /= y
print(x)            # 2.5

# =
x, y = 10, 5
x **= y
print(x)            # 100000 -> 10^5

# -------------------------- Comparison Operators -------------------------
# [==] Equal
print(100 == 100)       # True
print(100 == 200)       # False
print(100 == 100.0)     # True

# [!=] Not Equal
print(100 != 100)       # False
print(100 != 200)       # True
print(100 != 100.0)     # False

# [>] Greater Than
print(100 > 100)        # False
print(100 > 200)        # False
print(100 > 100.0)      # False

# [<] Less Than
print(100 < 100)        # False
print(100 < 200)        # True
print(100 < 100.0)      # False

# [>=] Greater Than or Equal
print(100 >= 100)       # True
print(100 >= 200)       # False
print(100 >= 100.0)     # True

# [<=] Less Than  or Equal
print(100 <= 100)       # True
print(100 <= 200)       # True
print(100 <= 100.0)     # True 
