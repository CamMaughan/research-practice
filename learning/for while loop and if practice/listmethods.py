# listmethods.py
# Author: C.Maughan
# Date: 8/4/24

# Reflection: I learnt how to use the append and pop methods for lists and how to reverse a string.
# I also learnt about the random module and how to use the randint function.

# Challenge 1: Uses random numbers between 1 and 10 (inclusive) to create a list with 5 integers

import random

list1 = []

for i in range(5):
    list1.append(random.randint(1, 10))

print(list1)

# Challenge 2: Removes a given index from a list.

remove_index = int(input("Enter the index you would like to remove from 0 to 4: "))

print(list1.pop(remove_index))

print(list1)

# Challenge 3: Reverse a given word.

word = input("Enter a word: ")

print(word[::-1])

# Challenge 4: Append another random number to list1 every secound for 6 secounds.

import time

for i in range(6):
    list1.append(random.randint(1, 10))
    time.sleep(1)

