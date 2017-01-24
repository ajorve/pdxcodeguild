"""
Calculate the smallest number of coins needed to represent an amount of cents
less than 100.

Hint: Keep a running total of the remainder as you write.

>>> make_change(94)
3 quarters
1 dimes
1 nickles
4 pennies

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
# 
# print('Amount of change to calculate in cents?')
# amount_cents = int(input())
#
# cents_left = amount_cents
# quarters = cents_left // 25
# cents_left = cents_left - quarters * 25
# dimes = cents_left // 10
# cents_left = cents_left - dimes * 10
# nickles = cents_left // 5
# cents_left = cents_left - nickles * 5
# pennies = cents_left
#
# print(str(quarters) + ' quarters')
# print(str(dimes) + ' dimes')
# print(str(nickles) + ' nickles')
# print(str(pennies) + ' pennies')
