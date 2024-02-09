# ------------------------------------ Dictionary ------------------------------------
# Dictionary items are enclosed in curly braces
user = {}

# Dictionary items are Contains key : value
user = {
    "Name" : "Anas",
    "Age" : 20,
    "Country" : "Egypt"
}

# Dictionary key need to be Immutabel -> (Number, String, Tuple), List not allowed
user = {
    "Name" : "Anas",
    "Age" : 20,
    "Country" : "Egypt",
    # [1, 2, 3, 4] : "List" -> TypeError: unhashable type: 'list'
}

# Dictionary value can have any data types
user = {
    "Name" : "Anas",
    "Age" : 20,
    "Country" : "Egypt",
    "Skills" : ["C++", "Python"],
    "Rating" : 2.93
}
print(user)                             # {'Name': 'Anas', 'Age': 20, 'Country': 'Egypt', 'Skills': ['C++', 'Python'], 'Rating': 2.93}

# Dictionary key need to be Unique
user = {
    "Name" : "Anas",
    "Age" : 20,
    "Country" : "Egypt",
    "Name" : "Anoos"
}
print(user)                             # {'Name': 'Anoos', 'Age': 20, 'Country': 'Egypt'}

# Dictionary is not ordered, You access its items with key
user = {
    "Name" : "Anas",
    "Age" : 20,
    "Country" : "Egypt",
}
print(user["Country"])                  # Egypt
print(user.get("Country"))              # Egypt
print(user.keys())                      # dict_keys(['Name', 'Age', 'Country'])
print(user.values())                    # dict_values(['Anas', 20, 'Egypt'])     

# ---------------------------- Two-Dimensional Dictionary ----------------------------
langueges = {
    "languege1" : {
        "Name" : "C++",
        "Progress" : "60%"
    },
    "languege2" : {
        "Name" : "Python",
        "Progress" : "20%"
    }
}
print(langueges)                        # {'languege1': {'Name': 'C++', 'Progress': '60%'}, 'languege2': {'Name': 'Python', 'Progress': '20%'}}

# Two-Dimensional Dictionary Access
print(langueges["languege1"])           # {'Name': 'C++', 'Progress': '60%'}
print(langueges["languege2"])           # {'Name': 'Python', 'Progress': '20%'}
print(langueges["languege2"]["Name"])   # Python

# Two-Dimensional Dictionary Length
print(len(langueges))                   # 2
print(len(langueges["languege1"]))      # 2
print(len(langueges["languege1"]["Name"]))  # 3

# Create dictionary from variables
languege1 = {
    "Name" : "C++",
    "Progress" : "60%"
}
languege2 = {
    "Name" : "Python",
    "Progress" : "20%"
}
langueges = {
    "languege1" : languege1,
    "languege2" : languege2
}
print(langueges)                        # {'languege1': {'Name': 'C++', 'Progress': '60%'}, 'languege2': {'Name': 'Python', 'Progress': '20%'}}

# ---------------------------- Dictionary Methods ------------------------------------
# Clear()
a = {
    "Name" : "Anas",
    "Age" : 20,
}
print(a)                                # {'Name': 'Anas', 'Age': 20}
a.clear()
print(a)                                # {}

# Update
a = {
    "Name" : "Anas",
}
print(a)                                # {'Name': 'Anas'}
a.update({"Age" : 20})                  # a["Age"] = 20
print(a)                                # {'Name': 'Anas', 'Age': 20}

# Copy()
a = {
    "Name" : "Anas",
}
b = a.copy()
print(a)                                # {'Name': 'Anas'}
print(b)                                # {'Name': 'Anas'}
a.update({"Age" : 20})
print(a)                                # {'Name': 'Anas', 'Age': 20}
print(b)                                # {'Name': 'Anas'}

# serDefault
a = {
    "Name" : "Anas",
}
print(a)                                # {'Name': 'Anas'}
print(a.setdefault("Name", "Islam"))    # Anas
print(a.setdefault("Age", "21"))        # 21
print(a)                                # {'Name': 'Anas', 'Age': '21'}

# popItem
a = {
    "Name" : "Anas",
    "Age" : 20,
    "Country" : "Egypt"
}
print(a)                                # {'Name': 'Anas', 'Age': 20, 'Country': 'Egypt'}
print(a.popitem())                      # ('Country', 'Egypt')
print(a)                                # {'Name': 'Anas', 'Age': 20}

# items()
a = {
    "Name" : "Anas"
}
user = a.items()
print(a)                                # {'Name': 'Anas'}
print(user)                             # dict_items([('Name', 'Anas')])
a["Age"] = 20
print(a)                                # {'Name': 'Anas', 'Age': 20}
print(user)                             # dict_items([('Name', 'Anas'), ('Age', 20)])

# fromkeys()
a = ("One", "Two", "Three")
b = 0
print(dict.fromkeys(a, b))              # {'One': 0, 'Two': 0, 'Three': 0}