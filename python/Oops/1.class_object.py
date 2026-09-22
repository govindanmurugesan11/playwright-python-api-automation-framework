"""
Topic: Class and Object

A class is a blueprint.
An object is an instance of a class.
"""


class Employee:

    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        print(self.name, self.role)


emp1 = Employee("Govindan", "QA Engineer")

emp1.display()    # Govindan QA Engineer