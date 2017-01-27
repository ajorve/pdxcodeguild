"""
Objective
Write a simple program that reads in a file containing some JSON and prints out some of the data.

1. Create a new directory called json-reader
2. In your new directory, create a new file called main.py

The output to the screen when the program is run should be the following:

The Latitude/Longitude of Portland is 45.523452/-122.676207.

'/Users/Anders/Desktop/PDX_Code/practice/json-reader/json_text.txt', {'Portand' : {'Latitude' : '45.523452/-122.676207', 'Longitude' : '-122.676207 '}}

"""
import json


def save(filename, data):
    """
    Take a dict as input, serializes it, then the serialized version of the dict saves to the specified filename.
    """
    data = input('Enter in the information you would like to write to this file.')
    with open(filename, 'w') as file:
        serialized = json.dumps(data)
        file.write(serialized)

save(filename, data)


def load(filename):
    """
    Takes a filename
    """
    with open(filename, 'r') as file:
        raw_data = file.read()
        data = json.loads(raw_data)
        return data
load(filename)
