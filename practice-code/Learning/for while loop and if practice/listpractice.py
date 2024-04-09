# listpractice.py
# Author: C.Maughan
# Date: 8/4/24

list_1 = [23, 66, 23, 12]
list_2 = [1, 19, 4, 8]
list_3 = ["land of", "the", "the long white cloud"]

# Challenge 1: Sum or Average of the lists.

sum_or_average = input("Would you like the sum or average of the lists? ")

if sum_or_average.strip().lower().find("sum") != -1:
    print(f"The sum of list 1 is {sum(list_1)}")
    print(f"The sum of list 2 is {sum(list_2)}")
elif sum_or_average.strip().lower().find("average") != -1:
    print(f"The average of list 1 is {sum(list_1) / len(list_1)}")
    print(f"The average of list 2 is {sum(list_2) / len(list_2)}")
else:
    print("Invalid input, please state either sum or average.")

# Assertions:
# sum_or_average = sum - then the sum of the lists will be printed. list 1 = 124, list 2 = 32
# sum_or_average = average - then the average of the lists will be printed. list 1 = 31, list 2 = 8

# Challenge 2: Get the smallest number from list 1.

smallest_number = list_1[0]

for number in list_1:
    if number < smallest_number:
        smallest_number = number
print(f"The smallest number in list 1 is {smallest_number}")

# Assertions:
# list_1 = [23, 66, 23, 12] - then the smallest number in list 1 is 12

# Challenge 3:  Randomly selects 2 integers from list_2 (the selected elements can be the same)

import random

random_number_1 = random.choice(list_2)
random_number_2 = random.choice(list_2)

print(f"The first random number is {random_number_1}. The second random number is {random_number_2}.")

# Assertions:
# list_2 = [1, 19, 4, 8] - then two random numbers will be selected from list_2

# Challenge 4: Outputs the strings from list_3 in the order from shortest to longest, and formatted as a single string.

list_3.sort(key=len)
print(" ".join(list_3))
print(list_3)
# Assertions:
# list_3 = ["land of", "the", "the long white cloud"] - then the output will be "the land of the long white cloud"