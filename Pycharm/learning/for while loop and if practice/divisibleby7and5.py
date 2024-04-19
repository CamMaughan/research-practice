# divisibleby7and5.py
# Author: C.Maughan
# Date: 2/4/24

# Reflection: As of exercise solution answer is correct - though a good idea is to /
# append n to a list. can join them after converting them into str by  /
# using the ','.join(list) - this joins the str with a comma from the  /
# variable 'list'.

# Finds the numbers between 1500 and 2700 that are divisible by 5 and 7

for n in range(1500,2701):
    if (n % 7 == 0) and (n % 5 == 0):
        print(n, end=" ")

