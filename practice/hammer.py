"""
Write a function that returns the meal for any given hour of the day.

Breakfast: 7AM - 9AM
Lunch: 12PM - 2PM
Dinner: 7PM - 9PM
Hammer: 10PM - 4AM

>>> meal(7)
'Breakfast time.'
>>> meal(13)
'Lunch time.'
>>> meal(20)
'Dinner time.'
>>> meal(21)
'Dinner time.'
>>> meal(0)
'No meal scheduled at this time.'
>>> meal(3)
'Hammer time.'
>>> meal(9999)
'Not a valid time.'

"""

def meal(time):
    time = input ("What hour of the day is it? >>")

    if in (7, 8, 9):
        message = "'Breakfast time.'"
    elif in (12, 13, 14):
        message = "'Lunch time.'"
    elif in (19, 20, 21):
        message = "'Dinner time.'"
    elif in (22, 23, 24, 1, 2, 3, 4):
        message = "'Hammer time.'"
    elif  in == 0:
        message = "'No meal scheduled at this time.'"
    else  in list(range(25, 9999)):
        message ="'Not a valid time.'"
    print(message)
