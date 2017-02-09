"""
Reverse Guess the number
Write a module that asks the user to enter a number 1 and 4 billion.
Create a range from 1 to 4 billion.
Have the computer guess the number until it has gotten it correct.
Hint: Use binary search!

"""

def guess_my_number():
    """
    Uses binary search to guess the number
    """

    high = 4_000_000_000
    low = 1
    comp_guess = 2_000_000_000
    guess_count = 0

    while True:
        response = input(f"Is your number {comp_guess}? Enter 'h' for higher, 'l' for lower or y for 'yes':  ")

        if response == 'y':
            print(f"Thanks for playing, it only took {guess_count} many times!")
            break

        elif response == 'l':
            high = comp_guess

        elif response == 'h':
            low = comp_guess

        comp_guess = (high + low) // 2
        guess_count += 1

guess_my_number()
