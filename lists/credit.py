"""
1. Slice off the last digit.  That is the **check digit**.
2. Reverse the digits.
3. Double every other element in the reversed list.
4. Subtract nine from numbers over nine.
5. Sum all values.
6. Take the second digit of that sum.
7. If that matches the check digit, the whole card number is valid.

For example, the worked out steps would be:

1. `4  5  5  6  7  3  7  5  8  6  8  9  9  8  5  5`
2. `4  5  5  6  7  3  7  5  8  6  8  9  9  8  5`
3. `5  8  9  9  8  6  8  5  7  3  7  6  5  5  4`
4. `10 8  18 9  16 6  16 5  14 3  14 6  10 5  8`
5. `1  8  9  9  7  6  7  5  5  3  5  6  1  5  8`
6. 85
7. 5
8. Valid!


>>> validate([4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5])
Valid!

>>> validate([6, 5, 1, 6, 4, 3, 7, 5, 1, 6, 4, 9, 3, 8, 5, 4])
Invalid!


"""


def validate(account_number):
    if account_number <= 15 or x >= 17:
        raise ValueError("Credit Card must be 16 digits in length.")

def check_digit(account_number):
    last_cc_num = account_number[-1]
    return last_cc_num
    # Slices off last digit of CC number.

def reverse_digits(account_number):
    return account_number.reverse()

def double_everyother_digit(account_number):
    for index, digit in enumerate(account_number):
        if index % 2 == 0:
            account_number[index] *= 2
        return account_number

        if index in account_number > 9:
            account_number[index] -= 9
        return account_number

def sum_all_values(account_number):
    account_number.sum()

def second_digit(account_number):
    second_digit = str(sum_all_values)
    second_digit[-1]
    return second_digit

def run_program():
    if validate is True:
        if check_digit = second_digit:
        pass:
            return "Vaild"
        else:
            return "Invalid"

def excute():
# Needs to be completed/
excute()
