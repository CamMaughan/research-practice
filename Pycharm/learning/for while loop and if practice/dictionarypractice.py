# dictionarypractice.py
# Author: C.Maughan
# Date: 8/4/24

# Reflection: A simple practice that has helped me understand the value of dictionaries in Python.
# Dictionaries are a powerful data structure that allows you to store data in key-value pairs.

# Challenge 1: Adds a stored dictionary item to a stored dictionary.

dict1 = {1: "kowabunga", 2: "cowabunga", 3: "kowabunga dude", 4: "cowabunga dude", 5: "kowabunga dude!",
         6: "cowabunga dude!"}

dict1_additon = {7: "kowabunga my dude!"}

dict1.update(dict1_additon)
print(dict1)

# Challenge 2: Removes a stored dictionary item from a stored dictionary.

dict1.pop(7)
print(dict1)

# Challenge 3: Outputs all contents of a stored dictionary.

for key, value in dict1.items():
    print(key, value)