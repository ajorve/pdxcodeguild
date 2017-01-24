"""
Fancy Phone numbers

Write a small app that asks the user for an all-digits phone number. THen pretty prints it out.

IN => 5035551234
OUT => 503-555-1234 or (503) 555-1234

"""
from pprint import pprint as pp


def fancy_phone():
    before_number = input("Please enter a phone number:  ")
# check for vaild number format
    number = str(before_number)
    print('Here is your number: {first}-{second}-{last} and ({first})-{second}-{last}'.format(first=number[0:3], second=number[3:6], last=number[6:10]))

fancy_phone()
