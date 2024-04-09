# cuboidmeasurements.py
# Author: C.Maughan
# Date: 1/4/24

# This program will allow the user to choose if calculating the surface   /
# area or the volume of given measurements for a cuboid.

def cuboid_surface_area(x, y, z):
    surface_area = round(2*((x*y) + (x*z) + (y*z)), 2)
    print(f"The surface area of the cuboid is: {surface_area}cm^2")

def cuboid_volume(x,y,z):
    volume = round(x * y * z, 2)
    print(f"The volume of the cuboid is: {volume}cm^3")

choice = input("Would you like to calculate the cuboids volume or surface area?: ")

if choice.lower().strip() == "volume":
    length = float(input("What is the length of the cuboid in cm?: "))
    width = float(input("What is the width of the cuboid in cm?: "))
    height = float(input("What is the height of the cuboid in cm?: "))
    cuboid_volume(length, width, height)
elif choice.lower().strip() == "surface area":
    length = float(input("What is the length of the cuboid in cm?: "))
    width = float(input("What is the width of the cuboid in cm?: "))
    height = float(input("What is the height of the cuboid in cm?: "))
    cuboid_surface_area(length, width, height)
else:
    print("Please choose either surface area, or volume")

# My assertions are:
# 1: For surface area - with length 4 - width 6 - height 8 - surface area /
# = 208cm^2
# 2: For volume with length 9 - width 200 - height 23.5 - volume =42,300  /
# cm^3
# 3: for surface are with length 4.78 - height 2.35 - height 2.89 - surfa /
# ce area = 63.68
