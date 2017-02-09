"""
Close, but Far!
Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more.
In: 1, 2, 10 =>  Out: True
In: 1, 2, 3 =>  Out: True
In: 4, 1, 3 =>  Out: True
In: 4, 11, 34 =>  Out: False

"""


def close_but_far(one, two, three):
    """
    >>> close_but_far([1, 2, 10])
    True
    """
    nums = input(list())
    a = nums[0]
    b = nums[1]
    c = nums[2]

    if abs(a - c) <= 1:
        if abs(b - c) >= 2:
            return True
        else:
            return False

    elif abs(a - b) <= 1:
        if abs(a -c) >= 2:
            return True
        else:
            return False

    else:
        return False

