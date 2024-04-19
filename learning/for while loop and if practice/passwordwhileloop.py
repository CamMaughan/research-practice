# passwordwhileloop.py
# author: C.Maughan
# date: 2/4/24

# Prompts user for password - gives three attempts - if user types exit /
# program finishes.

password = "exit"
attempts = 0

while attempts < 3:
    users_guess = input("What is the password?: ")
    if users_guess == password:
        print("That is the correct password.")
        break
    else:
        print("Password incorrect.")
        attempts += 1
