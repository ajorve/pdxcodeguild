"""## Python

- If you cut a white cable you can't cut white or black cable.
- If you cut a red cable you have to cut a green one next.
- If you cut a black cable it is not allowed to cut a white, green or orange one
- If you cut an orange cable you should cut a red or black one
- If you cut a green one you have to cut a orange or white one
- If you cut a purple cable you can't cut a purple, green, orange or white cable


```
In: [white, red, green, orange] => Out: 'Defused'
In: [white, orange, green, white] => Out: 'Boom'
```

"""
import re


def bomb_defuser():
    wire_colors = ['white', 'red', 'black', 'orange', 'green', 'purple']

    while user_input() == True:
        if user_input() == wire_colors[0]:
            user_input()
            if user_input() == wire_colors[]

    print("Defused")
    print("Boom!")

def user_input():
    wire_option = input("Please enter a color to cut!:  ")
    return wire_option


def defuse_checker():
