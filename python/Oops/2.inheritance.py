"""
Topic: Inheritance

Child class inherits properties and methods
from the parent class.
"""


class Vehicle:

    def start(self):
        print("Vehicle Started")


class Car(Vehicle):

    def drive(self):
        print("Car Driving")


car = Car()

car.start()    # Vehicle Started
car.drive()    # Car Driving
