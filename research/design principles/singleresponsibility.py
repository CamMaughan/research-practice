# singlereponsibility.py
# Author: Hiral Amodia
# Date: 5/10/2020

# This is code I have found from a repository on GitHub which provides examples of the SOLID principles.
# The code is an example of the Single Responsibility Principle.
# The code breaks the principle as the class TelephoneDirectory has multiple responsibilities.
# The class is responsible for managing the telephone directory, saving the contents to a file
# and persisting the contents to a database. The issue is the overlap in responsibilities. If one
# method is updated, it may affect the other methods. The class should be broken down into separate
# classes to handle the different responsibilities. Which I will show further down.


class TelephoneDirectory:
    def __init__(self):
        self.telephonedirectory = {}

    def add_entry(self, name, number):
        self.telephonedirectory[name] = number

    def delete_entry(self, name):
        self.telephonedirectory.pop(name)

    def update_entry(self, name, number):
        self.telephonedirectory[name] = number

    def lookup_number(self, name):
        return self.telephonedirectory[name]

    def save_to_file(self, file_name, location):
        # code to save the contents of telephonedirectory dictionary to the file
        pass

    def persist_to_database(self, database_details):
        # code to persist the contents of telephonedirectory dictionary to database
        pass

    def __str__(self):
        ret_dct = ""
        for key, value in self.telephonedirectory.items():
            ret_dct += f'{key} : {value}\n'
        return ret_dct


myTelephoneDirectory = TelephoneDirectory()
myTelephoneDirectory.add_entry("Ravi", 123456)
myTelephoneDirectory.add_entry("Vikas", 678452)
print(myTelephoneDirectory)

myTelephoneDirectory.delete_entry("Ravi")
myTelephoneDirectory.add_entry("Ravi", 123456)
myTelephoneDirectory.update_entry("Vikas", 776589)
print(myTelephoneDirectory.lookup_number("Vikas"))
print(myTelephoneDirectory)


# Below I will break the class into separate classes to handle the different responsibilities. Passing the
# telephonedirectory dictionary to the other classes to handle the different responsibilities.
# Firstly one class responsible for managing the telephone directory.


class TelephoneDirectory:
    def __init__(self):
        self.telephonedirectory = {}

    def add_entry(self, name, number):
        self.telephonedirectory[name] = number

    def delete_entry(self, name):
        self.telephonedirectory.pop(name)

    def update_entry(self, name, number):
        self.telephonedirectory[name] = number

    def lookup_number(self, name):
        return self.telephonedirectory[name]


# Secondly a class responsible for saving the contents of the telephone directory to a file.


class SaveToFile:
    def __init__(self, file_name, location):
        self.file_name = file_name
        self.location = location

    def save_to_file(self, telephonedirectory):
        # code to save the contents of telephonedirectory dictionary to the file
        pass


# Lastly a class responsible for persisting the contents of the telephone directory to a database.


class PersistToDatabase:
    def __init__(self, database_details):
        self.database_details = database_details

    def persist_to_database(self, telephonedirectory):
        # code to persist the contents of telephonedirectory dictionary to database
        pass
