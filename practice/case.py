"""

>>> snake_to_camel('this_is_snake_case')
'ThisIsSnakeCase'
>>> which_case('this_test_text')
'snake_case.'
>>> which_case('this_is_snake_case')
'snake_case.'
>>> which_case('ThisIsCamelCase')
'CamelCase.'

"""

# 3 Functions of looping

def snake_to_camel(word):
    word = word.replace('_', ' ').title().replace(' ', '')
    return(word)

def which_case(word):
    if '_' in word:
        return "snake_case."
    else:
        return "CamelCase."

    return result


