# functionswithparameters.py
# Author: C.Maughan
# Date: 10/4/24

# Challenge 1: A function with user input x and y integers and returns the first y multiiples of x

def multiples():
    x = int(input("Enter a number for x: "))
    y = int(input("Enter a number for y: "))
    for i in range(1, y + 1):
        print(x * i, end=", ")

multiples()

# Assertions:
# x = 2, y = 3 then output is 2, 4, 6
# x = 5, y = 4 then output is 5, 10, 15, 20

# Challenge 2: A function that calculates and displays the number of upper and lowercase letters in a stored string.

def count_case_letters():
    user_string = input("\nPlease enter a set of text:")
    lower_case = 0
    upper_case = 0
    for letter in user_string:
        if letter.isupper():
            upper_case += 1
        elif letter.islower():
            lower_case += 1

    print("The number of uppercase letters is: ", upper_case)
    print("The number of lowercase letters is: ", lower_case)

count_case_letters()

# Assertions:
# user_string = "Hello World" then output is 2 uppercase and 8 lowercase
# user_string = "HeLLo WoRLd" then output is 6 uppercase and 4 lowercase

# Challenge 3: A function that sums all the numbers in a random list

import random

def random_list():
    list_of_numbers = [random.randint(1, 100) for i in range(random.randint(5, 15))]
    print(list_of_numbers)
    return(list_of_numbers)

def sum_list(input_list):
    sum = 0
    for number in input_list:
        sum += number
    return sum

print(sum_list(random_list()))