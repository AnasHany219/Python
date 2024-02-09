# ---------------- Loop For and Else ---------------- 
nums = range(0, 10)                     # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in nums:
    if(num & 1 == 0):
        print(f"Even: {num}")
else:
    print("The Even numbers are finished!")
for num in nums:
    if(num & 1 == 1):
        print(f"Odd : {num}")
else:
    print("The Odd  numbers are finished!")

# Continue
nums = range(0, 10)
for num in nums:
    if(num == 3):
        continue
    print(num)

# Break
nums = range(0, 10)
for num in nums:
    if(num == 3):
        break
    print(num)

# Pass
nums = range(0, 10)
for num in nums:
    if(num == 3):
        pass
    print(num)

