"""
# String Masking

Write a function, than given an input string, 'mask' all of the characters with a '#' except for the last four characters.
```
In: '1234' => Out: '1234'
In: '123456789' => Out: '#####6789'
"""


# def string_masking(nums_list):
#     """
#     >>> string_masking([1, 2, 3, 4, 5, 6, 7, 8, 9])
#     '#####6789'
#     """
#     nums_list = list(nums_list)
#
#     if len(nums_list) <= 4:
#         return nums_list
#
#     else:
#         masked_list = list()
#         for num in nums_list[-4:]:
#             masked_list.append(str(num))
#
#         for _ in nums_list[:-5]:
#             masked_list.append('#')
#
#         result = "".join(masked_list[::-1])
#
#     return result
#         # nums_masked = [str(num) if num in nums_list[-4:] else '#' for num in nums_list]
#         # return nums_masked
#

def string_masking(nums_list):
    """
    >>> string_masking([1, 2, 3, 4, 5, 6, 7, 8, 9])
    '#####6789'
    """
    nums_list.reverse()                            #  Reversing

    result = list()
    for index, number in enumerate(nums_list):
        if index not in (0, 1, 2, 3):
            result.append('#')
        else:
            result.append(str(number))                 # Putinem back

    result.reverse()
    final_result = "".join(result)

    return final_result