# editingstr.py
# Author: C.Maughan
# Date: 12/4/24

# Reflection: I learnt how to use the join method and the choice function from the random module.

import random

# Challenge 1: Join a random character in a given string between each character in the string.


def random_join_string(string):
    random_char = random.choice(string)
    return random_char.joinstring


def main():
    user_string = input("Enter a string for the functions: ")
    challenge_choice = input("Enter the challenge number you would like to run: ")

    if challenge_choice == "1":
        print(random_join_string(user_string))


if __name__ == "__main__":
    main()