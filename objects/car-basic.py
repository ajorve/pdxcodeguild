"""
Create a class namned 'Car' to pass the doctests.

>>> my_car = Car()
>>> my_car.number_of_wheels
4
>>> my_car.color
'Black'
>>> my_car.number_of_doors
4
>>> my_car.honk()
honk

"""

class Car:
    def __init__(self, color, wheels, doors):
        self.color = color
        self.number_of_wheels = wheels
        self.doors = doors

    def __str__(self):
        return "{0.color} , #{0.wheels}, {0.doors} ".format(self)


    def honk(self):
        return "HONK!"
