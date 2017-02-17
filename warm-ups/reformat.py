"""
Reformat a number to that there are groups of three chars, followed by a dash. If the last group has only 1 char , reformat so that the last two groups have two chars.
IN: '922323454'
OUT: '922-323-454'

IN: '1223    -  -234--543'
OUT: '122-323-45-43'
"""
import re


def reformat():
    user_num = input("Please enter a number to be reformatted:  ")

    user_num_cleaned = re.sub(r'[\s*\-]', '', user_num)

    if user_num_cleaned % 3 != 0:
        result = [x for x in user_num_cleaned]

    else:
        result = "-".join(user_num_cleaned)


