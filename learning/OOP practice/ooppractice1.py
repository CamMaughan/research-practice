# ooppractice1.py
# Author: C.Maughan
# Date: 18/4/24

# Create a parent vehicle class then create a child 'Bus' class that inherits from the parent class.

class Vehicle:
    def __init__(self, make, model, year, color, capacity):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.capacity = capacity


class Bus(Vehicle):
    pass


bus1 = Bus('Ford', 'Transit', 2018, 'White', 15)

print("Make: ", bus1.make, "\nModel: ", bus1.model, "\nYear: ", bus1.year, "\nColor: ", bus1.color,
      "\nCapacity: ", bus1.capacity)

# The bus class inherits all the attributes of the parent class.