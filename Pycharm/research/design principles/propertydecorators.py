#Author: OMKAR PATHAK
# Date: 20/4/2020

#Without property decorators

class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        self.total= self.name+ " has "+self.balance+ " dollars in the account"

user1=BankAccount("Elon Musk","10000")
user1.name="Tim cook"
print(user1.name)
print(user1.total)

# Output: Tim cook
#         Elon Musk has 10000 dollars in the account

# The output is not as expected. The name is changed but the total amount is still shown for Elon Musk.
# This is because the total is calculated only once during the object creation in the __init__ method.

#With property decorators

class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    @property
    def total(self):
        return self.name+ " has "+self.balance+ " dollars in the account"

user1=BankAccount("Elon Musk","10000")
user1.name="Tim cook"
print(user1.name)
print(user1.total)

#Output: Tim cook
#        Tim cook has 10000 dollars in the account


# The output is as expected. The total is calculated every time the total attribute is accessed.
# This is because the total attribute is decorated with @property decorator.
# The @property decorator is used to make a method behave like an attribute.
# The total method is a getter method which is used to get the value of the total, but cannot
# be used to set the value of the total. Without the property decorator, the total method would
# have to be called as a method. But with the property decorator, it can be called as an attribute.

# The benefit of using property decorators is that it can set read only attributes that are calculated but
# not set. This adds a layer of security to the code through encapsulation.
