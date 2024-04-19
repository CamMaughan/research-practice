# dogyears.py
# Author: C.Maughan
# Date: 2/4/24


# Reflection: I learnt how to use an imbedded if statement in a for loop.

# Turns the given human years into dog years - first two human years equivalent to 10.5 dog years. After that 1:4 ratio.

def dog_age_converter(human_years):
    dog_years = float(0)
    human_years += 1
    for n in range(1, human_years):
        if n == 1 or n == 2:
            dog_years += 10.5
        else:
            dog_years += 4
    print(dog_years)


human_years = int(input("What is the dogs human age?: "))
dog_age_converter(human_years)

# My assertions:
# 1: Human years = 2 - dog years = 21
# 2: Human years = 3 - dog years = 25