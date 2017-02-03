"""

Create a car for color, plate # and doors.
Create a parking lot that will only fit to its capacity the cars created.

"""


class Vehicle:
    def __init__(self, color, plate, doors):
        self.color = color
        self.plate = plate
        self.doors = doors

    def __str__(self):
        return "{0.color} , #{0.plate}, {0.doors} ".format(self)

    @staticmethod
    def honk():
        return "HONK!"


class ParkingLot:

    def __init__(self, capacity, rate):
        self._capacity = capacity
        self.hourly_rate = rate
        self.available_spaces = capacity
        self.spaces = list()

    def park(self, vehicle):
        if len(self.spaces) <= self._capacity:
            self.spaces.append(vehicle)
            self.available_spaces -= 1
        else:
            return "Lot is Full"


