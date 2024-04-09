# numberwhileloop.py
# author: C.Maughan
# date: 2/4/24

# This program uses the while loop to take a positive integer from the /
# user then print from 1 to this number.

limit = input("Please choose a positive interger to print to: ")
counter = 1
sum = 0

while counter <= int(limit):
    print(f"[{counter}]", end = " ")
    sum += counter
    counter += 1

# Now will take the limit and add the total sum of all the numbers printed
print(sum)
