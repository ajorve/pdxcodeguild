"""
Here are the rules for the FizzBuzz problem:

Given the length of the output of numbers from 1 - n:
If a number is divisible by 3, append "Fizz" to a list.
If a number is divisible by 5, append "Buzz" to that same list.
If a number is divisible by both 3 and 5, append "FizzBuzz" to the list.
If a number meets none of theese rules, just append the string of the number.

>>> fizz_buzz(15)
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']


REMEMBER: Use Encapsulation! D.R.Y.
>>> joined_buzz(15)
'1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz'

"""

def fizz_buzz(stop_num):

    number_list = list()

    for each_number in range(1, stop_num + 1):

        if each_number % 3 == 0 and each_number % 5 == 0:  #if each_number % 15 == 0:
            number_list.append("FizzBuzz")

        elif each_number % 3 == 0:
            number_list.append("Fizz")

        elif each_number % 5 == 0:
            number_list.append("Buzz")

        else:
            number_list.append(each_number)

    return number_list


def joined_buzz(number):

    return " ".join(fizz_buzz(number))
