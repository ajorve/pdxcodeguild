"""
# Given an input list, exclude an input integer and it's following element.
>>> exclude_em([56, 57, 58, 59, 60], rem=57)
[56, 59, 60]


>>> exclude_em([43, 67, 456, 23, 878, 5, 65, 34], rem=456)
[43, 67, 878, 5, 65, 34]


# Remove the first two element by default.
>>> exclude_em([43, 67, 456, 23, 878, 5, 65, 34])
[456, 23, 878, 5, 65, 34]


# Given two lists of ints, multiply numbers located at the same index
# in thier respective lists by each other. If the reusult is zero, append -1 instead.
>>> double([43, 67, 456, 23, 878, 5, 65, 34], [2, 1, 1, 2, 2, 0, 0, 0])
[86, 67, 456, 46, 1756, -1, -1, -1]


# Given two lists and an int, insert the elements of a list into the first list at the nth position
>>> punch_in([43, 67, 456, 23, 878, 5, 65, 34], [2, 1, 1, 2, 2, 0, 0, 0], 2)
[43, 67, 2, 1, 1, 2, 2, 0, 0, 0, 456, 23, 878, 5, 65, 34]
"""

def exclude_em(nums, *num, rem=None):
    """
    Function that removes num and the following element from nums list.

    Default rem (remove) returns a list that removes elements from nums upto and including rem.
    """

    result = list()

    if rem is None:
        return nums[2::]
    else:
        bad_num = nums.index(rem)
        exclude_nums = bad_num, bad_num + 1

        out = list()
        for index, number in enumerate(nums):
            if index not in exclude_nums:
                out.append(number)
    return out

def double(nums1, nums2):
    """
    Multiplies the numbers in nums1 by nums2 and returns -1 if answer is 0.
    """

    nums1 = list(nums1)
    nums2 = list(nums2)

    result = list()

    for index, n in enumerate(nums1):
        result.append(nums1[index] * nums2[index])
        if result[-1] == 0:
            result[-1] = -1

    return result

def punch_in(nums1, nums2, ind):
    """
    Given two lists, insert the elements of the second list into the first one at the given index.
    """

    nums1[ind:ind] = nums2
    return nums1
