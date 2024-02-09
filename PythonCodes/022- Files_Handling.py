# ------------------------------------ Files Handling ------------------------------------ 
# Modes:
# "a"   Append  Open file for appending - Create If not exists
# "w"   Write   Open File for writing   - Create If not exists
# "r"   Read    Open File for reading   - Error  If not exists [Default value]
# "x"   Create  Craete file             - Error  If     exists 

file = open("file1.txt")

print(file)                         # <_io.TextIOWrapper name='file.txt' mode='r' encoding='cp1252'>
print(file.name)                    # file.txt
print(file.mode)                    # r
print(file.encoding)                # cp1252

file.close()
# ----------------------------------------- Read ----------------------------------------- 
file = open("file1.txt")

print(file.read())                  # Hello, dude! 
                                    # My name is Anas
print(file.read(5))                 # Hello

print(file.readline())              # Hello, dude!
print(file.readline())              # My name is Anas

print(file.readlines())             # ['Hello, dude! \n', 'My name is Anas']

file.close()

# ---------------------------------------- Write ----------------------------------------- 
file = open("file2.txt", "w")

file.write("Hello, Python! I love C++ \n")
file.write("Hello, Python! I love C++ \n" * 2)

list = ["Name: Anas \n", "Age: 20 \n"]
file.writelines(list)

file.close()

# --------------------------------------- Append -----------------------------------------
file = open("file2.txt", "a")

file.write("Hello, Python! I love C++ \n")
file.write("Hello, Python! I love C++ \n" * 2)

list = ["Name: Anas \n", "Age: 20 \n"]
file.writelines(list)

file.close()

# -------------------------------- Important Information ---------------------------------
file = open("file1.txt", "a")
file.truncate(5)                    # Clear all file but keep n chars
print(file.tell())                  # Return cursor position

file.write(", Anas")
file = open("file1.txt", "r")
file.seek(5)                        # Change cursor position
print(file.read())                  # , Anas
file.close()

# Remove files
import os
os.remove("file1.txt")
os.remove("file2.txt")