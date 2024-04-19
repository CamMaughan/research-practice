# returningfunctions.py
# Author: C.Maughan
# Date: 10/4/24

# Challenge 1: A stored list containing three other lists. If any list contains less than 3 elements, prompts user
# to enter more elements until the list contains 3 elements. Then, prints the list.

import time

list_a = ["brown", "grey", "amber"]
list_b = ["red", "green"]
list_c = ["purple"]
list_d = [list_a, list_b, list_c]


def check_list(list):
    for internal_list in list:
        while len(internal_list) < 3:
            internal_list.append(input(f"Please enter another value for {internal_list}: "))
    return list


print(check_list(list_d))

# Challenge 2: A count down function that takes a number and counts down to 0. If the number is negative, it should
# print "Please enter a positive number" and return None. The countdown should be in seconds.


def count_down(number):
    if number <= 0:
        print("Please enter a positive number")
        return None
    else:
        for i in range(number, -1, -1):
            print(i)
            time.sleep(1)


count_down(int(input("Please enter a number to count down from: ")))


# Challenge 3: Function that returns the first n numbers in the fibonacci sequence.

def fibonacci(n):
    fib_list = [0, 1]
    for i in range(2, n):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    return fib_list


print(fibonacci(int(input("Please enter a number to get the first n numbers in the fibonacci sequence: "))))


# Challenge 4: Checks if user input is a prime number

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(is_prime(int(input("Please enter a number to check if it is prime: "))))

