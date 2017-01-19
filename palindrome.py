"""
Write a function that returns True if the input is a palindrome, or False, if it is not.

>>> palindrome('hannah')
True

>>> palindrome('racecar')
True

>>> palindrome('a man, a plan, a canal, Panama')
True

>>> palindrome("1 pound coconut.")
False

>>> palindrome(1234321)
True

"""

def palindrome(word):

    word = str(word).lower() ##("What word would you like to check if it's a Palindrone?").lower()

    word= str(word).replace(',', '').replace(' ','')

    if word[::-1] == word:
        return True
    else:
        return False

##palindrome(word)

## Finish this, i'm close..!
