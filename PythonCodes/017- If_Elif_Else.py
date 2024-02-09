# ----------------- If - Elif - Else ----------------- 

name = input("Enter Your Name:")
if name[0] >= 'A' and  name[0] <= 'B':
    print(f"Your first character is \"{name[0]}\"") 
elif name[0] >= 'C' and  name[0] <= 'L':
    print(f"Your first character is \"{name[0]}\"")
else :
    print(f"Your first character is \"{name[0]}\"")

# ----------------- Ternary IF ----------------- 
movieRate = 18
age = 16
print("The movie is good 4U" if age >= movieRate else "The movie is not good 4U")
