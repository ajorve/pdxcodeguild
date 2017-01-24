"""
Given a list of integers, find all pairs of numbers that when added equals the sum.

>>> find_sum_pairs([-1, 0, 1, 2], 3)
[[1, 2]]

>>> find_sum_pairs([-1, 0, 1, 2], 1)
[[-1, 2], [0, 1]]

>>> find_sum_pairs([2, -1, 2], 1)
[[2, -1], [-1, 2]]

>>> find_sum_pairs([-1, 1, 2, 2], 3)
[[1, 2], [1, 2]]

"""

def find_sum_pairs(nums, x_sum):
    """
    Returns a list of pairs from nums of numbers that add up to the num.
    """


    result = [[n, i] for n in nums for i in nums if n+i == x_sum]

    if result == result[::-1]:
        result = result[:len(result)//2]

    else:
        for i in result:
            for index, n in enumerate(result):
                if i == n[::-1]:
                    result.pop(index)


    return result
