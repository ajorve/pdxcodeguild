"""
This is a Multiline Comment. THis is the first thing in the file.
AKA 'Module' Docstring.
"""


def change():
    amount = input(int("What is the amount of money you have?"))
    dollars = amount // 100
    rem = amount - dollars * 100
    quarters = rem // 25
    rem = rem - quarters * 25
    dimes = rem // 10
    rem = rem - dimes * 10
    nickels = rem // 5
    rem = rem - nickels * 5
    pennies = rem

    print("{} Dollars, {} Quarters, {} Dimes, {} Nickels, {} Cents change").format(dollars, quarters, dimes, nickels, pennies)

change()


