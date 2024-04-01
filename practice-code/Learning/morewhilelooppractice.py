# morewhilelooppractice.py
# author: C.Maughan
# date: 2/4/24

# Prompts user to calculate the area or volume of an abstract shape. Or to /
# exit the program. Repeats displaying the options until user types exit. /
# Also prompts user for two integers for measurements of the shape,       /
# within an accepted range.

def shape_volume(x, y):
    if (x >= 1) and (x <= 8) and (y >= 1) and (y <= 7):
        cuboid_height = 8 - y
        cuboid_width = 3
        cuboid_length = 10
        cuboid_volume = cuboid_width * cuboid_length * cuboid_height

        small_cuboid_height = y
        small_cuboid_width = 3
        small_cuboid_length = (10-x)/2
        small_cuboid_volume = (small_cuboid_length * small_cuboid_width *
                               small_cuboid_height)

        total_volume = (small_cuboid_volume * 2) + cuboid_volume
        print(f"The shapes volume with input {x} and {y} is {total_volume}cm^3")
    else:
        print("Please enter viable x and y measurements.")

def shape_area(x, y):
    if (x >= 1) and (x <= 8) and (y >= 1) and (y <= 7):
        cuboid_height = 8 - y
        cuboid_width = 3
        cuboid_length = 10
        cuboid_area = 2 * ((cuboid_height * cuboid_width) + (cuboid_width *
                            cuboid_length) + (cuboid_height * cuboid_length))
        small_cuboid_height = y
        small_cuboid_width = 3
        small_cuboid_length = (10 - x) / 2
        small_cuboid_area = 2 * ((small_cuboid_height * small_cuboid_width) +
                                 (small_cuboid_width * small_cuboid_length) +
                                 (small_cuboid_height * small_cuboid_length))
        total_area = (2 * small_cuboid_area) + cuboid_area
        print(f"The shapes area with input {x} and {y} is {total_area}cm^2")
    else:
        print("Please enter viable x and y measurements.")

print("Welcome to the abstract shape calculator!")
print("The shape being calculated can be found on the corresponding "
      "page on github. This also shows the positions of the requested "
      "measurements.")
print("We will check whether you wish to calculate the shapes volume or "
      "area. Then we will ask for your values to x and y."
      " If these values area invalid we will indicate this."
      " If you wish to exit the program, simply type 'exit'.")

program_running = True


while program_running:
    user_input = input("Do you wish to calculate the area, volume or exit?: ")
    if user_input.lower().strip() == "exit":
        program_running = False
    elif user_input.lower().strip() == "volume":
        x = int(input("What is x in cm?: "))
        y = int(input("What is y in cm?: "))
        shape_volume(x,y)
    elif user_input.lower().strip() == "area":
        x = int(input("What is x in cm?: "))
        y = int(input("What is y in cm?: "))
        shape_area(x, y)

# My assertions:
# 1: area -  x = 20 y = 13 - will prompt user to enter viable measurements/
# then will ask the initial options again.
# 2: area - x = 1 and y = 1 - area = 326cm^2
#3: volume - x = 5 and y = 3 - volume = 195cm^3.