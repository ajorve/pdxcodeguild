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
    if time >= 22 and time <= 4:
        return "Hammer time."
    elif time >= 7 and time <= 9:
        return "Breakfast time."
    elif time >= 12 and time <= 14:
        return "Lunch time."
    elif time >=19 and time <= 21:
        return "Dinner time."
    elif time >= 25:
        return "Not a valid time."
    elif time <= 0 or time >=24:
        return "No meal scheduled at this time."
    else:
        return "Hammer time."
