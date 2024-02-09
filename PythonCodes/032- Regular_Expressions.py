# -------------------------------------- Regular Expressions --------------------------------------
# [1] Sequence of characters that define a search pattern
# [2] Regular Expressions is not in python its a general concept
# [3] Used in [IP Address validation, Email Validation, Creidt card validation]
# [4] Test regex:- https://pythex.org/
# [5] Character sheet:- https://www.debuggex.com/cheatsheet/regex/python

# ------------------------------------------ Quantifiers ------------------------------------------
# *	0 or more
# +	1 or more
# ?	0 or 1
# {2}	Exactly 2
# {2,5}	Between 2 and 5
# {2,}	2 or more
# (,5}	Up to 5

# -------------------------------------- Characters Classes ---------------------------------------
# [0-9]
# [^0-9]
# [A-Z]
# [^A-Z]
# [a-z]
# [^a-z]

# ------------------------------------------ Assertions -------------------------------------------
# ^ Start of string
# $ End of string

# ----------------------------------------- Email Match -------------------------------------------
# [A-z0-9\.]+@[A-z0-9]+\.[A-z]
# ^[A-z0-9\.]+@[A-z0-9]+\.(com|net|org)$

# ----------------------------------- Logical Or and Escaping -------------------------------------
# |     -> OR
# \     -> Escape Special Characters
# ()    -> Seperate Groups

# ---------------------------------- Re Module Search and FindAll ---------------------------------
# search()          -> Search a string for a match and return the fisrt match only
# findall()         -> Return list of all matches and Empty list if none
# Email pattern     -> [A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)

import re
s = re.search("[A-Z]", "Anas Hany Shaaban Gad")
print(s)                                # <re.Match object; span=(0, 1), match='A'>
print(s.span())                         # (0, 1)
print(s.string)                         # Anas Hany Shaaban Gad
print(s.group())                        # A

# ---------------------------------- Re Module Split() and Sub() ----------------------------------
# Split(Pattern, string, MaxSplit)              -> Return A List of elements splitted on each match
import re
s1 = "Love C++"
s2 = "How-Are_You-?"
search1 = re.split(r"\s", s1, 1)
search2 = re.split(r"-|_", s2)
print(search1)                          # ['Love', 'C++']
print(search2)                          # ['How', 'Are', 'You', '?']

# Sub(Pattern, Replace, String, ReplaceCount)   -> Replace Matches with what you want
print(re.sub(r"-|_", r" ", s2, 3))      # How Are You ?

