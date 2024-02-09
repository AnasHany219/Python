# syntax -> [Variabl Name] [Assignment Operator] [Vlaue] 

# ------------------------------------------------------
# Name Convention and Rules:

# -> [1] Can start with [a-z A-Z] or Underscore "_"
var = "value"
_var = "value"

# -> [2] Cannot start with [0-9] or Special Characters
# 0var = "value"  -> error
# -var = "value"  -> error

# -> [3] Can include [0-9]
var1 = "value"

# -> [4] Cannot include Special Characters
# var- = "value"

# -> [5] var is not like Var [Case Sensitive]
Var = "value"

# ------------------------------------------------------
# Cases for Variable names:
name = "Anas Hany"      # Single word   -> Normal
myName = "Anas Hany"    # Two words     -> camelCase
my_name = "Anas Hany"   # Two words     -> snake_case

# ------------------------------------------------------
# Reserved Words
help("keywords")

# ------------------------------------------------------
# multi initial
a, b, c = 1, 2, 3
