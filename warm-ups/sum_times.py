"""
Weekly warmup

Given a list of 3 int values, return their sum.
However, if one of the values is 13 then it does not count towards the sum and values to its right do not count.
If 13 is the first number, return 0.
In: 1, 2, 3 => Out: 6
In: 5, 13, 6 => Out: 5
In: 1, 13, 9 => Out: 1

"""
import time


def sum_times(user_nums):
    """
    >>> sum_times([1, 3, 5])
    9
    >>> sum_times([13, 8, 9])
    0
    """

    nums = list()
    for num in user_nums:
        if num == 13:
            break
        else:
            nums.append(num)

    return sum(nums)


def collect_nums():
    """
    Collects user input, build a list of ints, and calls the sum_times function
    """
    nums = list()
    while True:

        answer = input("Please enter some numbers to find their SUM or type done:  ")

        if answer in ('q', 'quit', 'exit', 'done'):
            sum_times(nums)

        else:
            try:
                num = int(answer)
                nums.append(num)

            except ValueError:
                print("Invalid, please enter a number instead...")
                time.sleep(2)
                raise TypeError("Invalid, please enter a number instead.")

