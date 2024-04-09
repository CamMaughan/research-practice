# multiples.py
# author: C.Maughan
# date: 2/4/24

# The program prints multiples of a number from 10 until reaching /
# another given number (limit, which is inclusive)

starting_number = int(input("What is the number you wish to see multiples "
                            "of?: "))
limit = int(input("What is the limit for the multiples?: "))
counter = 1

while counter <= limit:
    if (counter >= 10) and (counter % starting_number == 0):
        print(counter, end=" ")
    counter += 1

# My assertions: 1: starting_number = 4 and limit = 29 output = 12 16 20 /
# 24 28
# 2: starting number = 10 limit = 50 output = 10 20 30 40 50
# 3: starting number = 12 limit = 36 output = 12 24 36