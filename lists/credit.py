"""
1. Slice off the last digit. That is the **check digit**.
1. Reverse the digits.
1. Double every other element in the reversed list.
1. Subtract nine from numbers over nine.
1. Sum all values.
1. Take the second digit of that sum.
1. If that matches the check digit, the whole card number is valid.

For example, the worked out steps would be:

1. `4  5  5  6  7  3  7  5  8  6  8  9  9  8  5  5`
1. `4  5  5  6  7  3  7  5  8  6  8  9  9  8  5`
1. `5  8  9  9  8  6  8  5  7  3  7  6  5  5  4`
1. `10 8  18 9  16 6  16 5  14 3  14 6  10 5  8`
1. `1  8  9  9  7  6  7  5  5  3  5  6  1  5  8`
1. 85
1. 5
1. Valid!


>>> run_program([4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5])
'Valid!'

>>> run_program([6, 5, 1, 6, 4, 3, 7, 5, 1, 6, 4, 9, 3, 8, 5, 4])
'Invalid!'

THIS IS A WORK IN PROGRESS
"""


def validate(account_number):
    """
    VALIDATOR
    """
    if len(account_number) <= 15 or len(account_number) >= 17:
        raise ValueError("This is not a valid CC number.")

    else:
        return True


def check_digit(account_number):
    last_cc_num = account_number[-1]
    return last_cc_num


def reverse_digits(account_number):
    account_number.reverse()
    return account_number


def double_every_other_digit(account_number):
    for index, num in enumerate(account_number):
        if index % 2 == 0:
            account_number[index] *= 2

    return account_number


def subtract_over_nine(account_number):
    for index, num in enumerate(account_number):
        if num > 9:
            account_number[index] -=9

    return account_number


def second_digit(account_number):
    first_second_digit = str(account_number)
    final_second_digit = first_second_digit[-1]
    return final_second_digit


def run_program(account_number):
    if validate(account_number) is True:
        last_cc_num = check_digit(account_number)
        account_number.pop()
        revd = reverse_digits(account_number)
        doubled = double_every_other_digit(revd)
        subbed = subtract_over_nine(doubled)
        summed = sum(subbed)
        std_second_digit = second_digit(summed)

        if last_cc_num == int(std_second_digit):
            result = "Valid!"
        else:
            result = "Invalid!"

    return result


#  THIS IS A WORK IN PROGRESS
run_program([4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5])