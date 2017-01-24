"""

Prime Numbers

Write a function to calculate the largest prime number up to 'n'. Return only the largest number in range.

"""
#
# def prime():
#     numbers = int(input("Enter number to find out if it's a Prime Number:  "))
#     largest = None
#     for num in range(2,numbers+1):
#         if x % num == 0:
#             is_prime = False
#         for x in range(1,is_prime+2):
#             if num % x == 0:
#                 is_prime = True
#                 break
#     print()
#
# prime()

prime_numbers = 0

def is_prime_number(x):
    x = int(input("Enter number to find out if it's a Prime Number:  "))
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
            else:
                return True


    for i in range(int(raw_input("How many numbers you wish to check: "))):
        if is_prime_number(i):
            prime_numbers += 1
            print(i)

is_prime_number()
