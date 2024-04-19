# variablescopepractice.py
# Author: C.Maughan
# Date: 10/4/24

# testing the passing of local variables to functions

def fun_a():
    name = "Alice"
    age = 25
    return name, age
# Testing that fun_b can name the fun_a variables whatever it wants and still get the same result
def fun_b():
    different, stuff = fun_a()
    print(different)
    print(stuff)

fun_b()



