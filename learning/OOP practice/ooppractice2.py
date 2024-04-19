# ooppractice2.py
# Author: C.Maughan
# Date: 18/4/24

# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of
# Bus.seating_capacity() a default value of 50.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers."


class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        # The super() function is used to call the parent class, and take the .seating_capacity() method caled with the
        # capacity=50 argument.
        return super().seating_capacity(capacity)


bus1 = Bus('Volvo', 180, 12)
print(bus1.seating_capacity())
