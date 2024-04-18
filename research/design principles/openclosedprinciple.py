# openclosedprinciple.py
# Author: Hiral Amodia
# Date: 5/10/2020

# Firstly,  below is the code showing what it looks like when the open/closed principle is not being followed.


# Open - Close Principle
# Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification

from enum import Enum
class Products(Enum):
  SHIRT = 1
  TSHIRT = 2
  PANT = 3

class DiscountCalculator():
  def __init__(self, product_type, cost):
    self.product_type = product_type
    self.cost = cost

  def get_discounted_price(self):
    if self.product_type == Products.SHIRT:
      return self.cost - (self.cost * 0.10)
    elif self.product_type == Products.TSHIRT:
      return self.cost - (self.cost * 0.15)
    elif self.product_type == Products.PANT:
      return self.cost - (self.cost * 0.25)

dc_Shirt = DiscountCalculator(Products.SHIRT, 100)
print(dc_Shirt.get_discounted_price())

dc_TShirt = DiscountCalculator(Products.TSHIRT, 100)
print(dc_TShirt.get_discounted_price())

dc_Pant = DiscountCalculator(Products.PANT, 100)
print(dc_Pant.get_discounted_price())


# The above code violates the Open Closed Principle because if a new product type is to be included,
# the class will need modification. Also if the discount percentage changes, the class will need modification.

# Below is the code that follows the Open Closed Principle.


from enum import Enum
from abc import ABCMeta, abstractmethod

# This abstract method is the most valuable part in keeping the code in compliance with the Open Closed Principle.
# Any class that extends DiscountCalculator will have to implement it own implementation of get_discounted_price.
# Allowing to create new subclasses for each new product type without modifying the existing code.
# To change the discount percentage, you can just create a new subclass and implement the get_discounted_price method.
# Or modify the existing subclass for a product, but this does not modify the existing code in the abstract method.
class DiscountCalculator():

  @abstractmethod
  def get_discounted_price(self):
    pass

# The below classes are a single product type. Each class has its own implementation of get_discounted_price.
class DiscountCalculatorShirt(DiscountCalculator):
  def __init__(self, cost):
    self.cost = cost

  def get_discounted_price(self):
      return self.cost - (self.cost * 0.10)

class DiscountCalculatorTshirt(DiscountCalculator):
  def __init__(self, cost):
    self.cost = cost

  def get_discounted_price(self):
      return self.cost - (self.cost * 0.15)

class DiscountCalculatorPant(DiscountCalculator):
  def __init__(self, cost):
    self.cost = cost

  def get_discounted_price(self):
      return self.cost - (self.cost * 0.25)

dc_Shirt = DiscountCalculatorShirt(100)
print(dc_Shirt.get_discounted_price())

dc_TShirt = DiscountCalculatorTshirt(100)
print(dc_TShirt.get_discounted_price())

dc_Pant = DiscountCalculatorPant(100)
print(dc_Pant.get_discounted_price())