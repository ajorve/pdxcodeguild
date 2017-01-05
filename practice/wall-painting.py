"""
This is a Multiline Comment. THis is the first thing in the file.
AKA 'Module' Docstring.
"""


def wall_painting():
    wall_width = int(input("What is the width of the wall?"))
    wall_height = int(input("What is the height of the wall?"))
    gallon_cost = int(input("What is the cost of the gallon"))
    gallon_covers= 400

    sq_footage = wall_width * wall_height
    gallon_total = sq_footage // gallon_covers
    cost = gallon_total * gallon_cost

    print("If will cost you ${} to paint this wall..".format(cost))

wall_painting()