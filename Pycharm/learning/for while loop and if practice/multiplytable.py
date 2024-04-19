# multiplytable.py
# Author: C.Maughan
# Date: 2/4/24

# Outputs multiplication table for n (user input) from 1 to 10.

users_number = int(input("Give an integer for the multiplication table: "))


for n in range(1,11):
    print(f"{users_number} x {n} = {users_number * n}")

# Assertions:
# 1: users_number = 1 - 1 x 1 = 1 | 1 x 2 = 2 | 1 x 3 = 3 etc....
# 2: users_number = 9 - 9 x 1 = 9 | 9 x 2 = 18 | 9 x 3 = 27 etc...