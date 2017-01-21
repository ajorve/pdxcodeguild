"""
Password check

User must meet criteria for password entered by having:

1. At least lowercase letter
2. At least 1 number
3. At least 1 uppercase letter
4. At least 1 special character
5. Min of length 6
6. Max length of 12

"""

import string
import re


def password_check():
    password_entered = input("Please enter a password that meets the criteria of x :  ")
    if len(password_entered) < 6 and len(password_entered) > 12:
        raise TypeError("Please enter a password that is between 6 and 12 characters long:  ")
        password_check()

    pattern = re.compile(r"""
                         ^.*
                         (?=.{12,})
                         (?=.*\d)
                         (?=.*[a-z])
                         (?=.*[A-Z])
                         (?=.*[@#$%^&+=])
                         .*$
                         """,re.VERBOSE)

    result = re.findall(pattern, password_entered)

    if (result):
        print("Valid password")
    else:
        print("Password not valid")

password_check()
