# todolist.py
# Author: C.Maughan
# Date: 19/4/24

'''

This program will be a basic to-do list program. It will allow the user to add, remove, and view tasks.
The tasks will be stored in a list. The user will be able to view the tasks in the list, add a task to the list,
and remove a task from the list. The user will also be able to quit the program. The program will run in a loop
until the user decides to quit.

My main goal for this program is to practice a way to clean up the main function. I will do this by creating a
class for the user interface, rather than making a bunch of code in the main function.

'''


class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        return f"{self.title} - {self.description} - Due: {self.due_date} - Completed: {self.completed}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                self.tasks.remove(task)
                break

    def mark_task_as_completed(self):
        if not self.tasks:
            print("No tasks to mark as completed")
            return
        while True:
            title = input("Enter task title: ")
            for task in self.tasks:
                if task.title == title:
                    task.mark_as_completed()
                    print(f"{task.title} marked as completed")
                    return
            print(f"Task with title {title} not found.\n"
                  f"Please enter a valid task title from the following: "
                  f"{[task.title for task in self.tasks]}")

    def display_tasks(self):
        for task in self.tasks:
            print(task)


class UserInterface:
    def __init__(self, to_do_list):
        self.to_do_list = to_do_list

    @staticmethod
    def display_main_menu():
        print("1. Add a task")
        print("2. Delete a task")
        print("3. Mark a task as completed")
        print("4. Display all tasks")
        print("5. Exit")

    def main_loop(self):
        while True:
            self.display_main_menu()
            choice = input("Enter choice: ")

            if choice == "1":
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                due_date = input("Enter task due date: ")
                task = Task(title, description, due_date)
                self.to_do_list.add_task(task)

            elif choice == "2":
                title = input("Enter task title: ")
                self.to_do_list.delete_task(title)

            elif choice == "3":
                self.to_do_list.mark_task_as_completed()

            elif choice == "4":
                self.to_do_list.display_tasks()

            elif choice == "5":
                break

            else:
                print("Invalid choice")


if __name__ == "__main__":
    to_do_list = ToDoList()
    user_interface = UserInterface(to_do_list)
    user_interface.main_loop()

'''

I believe putting the user interface in a class has made the main function much cleaner. As a result making the 
program easier to: read, debug, extend, and maintain. I am happy with the result of this program.

I also experimented with user input validation in this program. I used a while loop to keep asking the user for input
until they enter a valid input. As this was not the main goal of the program, I didn't do it for every input.

'''