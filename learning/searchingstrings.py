# searchingstrings.py
# Author: C.Maughan
# Date: 12/4/24

stored_string = "The first rule of fight club is: do not talk about fight club."

# Challenge 1: Return number of spaces in stored_string


def count_spaces(string):
    return string.count(" ")


print(count_spaces(stored_string))

# Challenge 2: Return total number of punctuations used in stored_string. e.g. full stops, colons, commas, etc.


def count_punctuations(string):
    punctuations = [".", ",", ":", ";", "!", "?"]
    count = 0
    for char in string:
        if char in punctuations:
            count += 1
    return count


print(count_punctuations(stored_string))

# Challenge 3: Return index position of first mention of 'fight' after the colon in stored_string

print(stored_string.find("fight", stored_string.find(":")))

# Challenge 4: Return if a given password meets the following checks: 8 characters long, contains a digit,
# contains an uppercase letter, contains a lowercase letter


def password_check(password):
    password = password.replace(" ", "")
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    return True


print(password_check(input("Enter a password: ")))
