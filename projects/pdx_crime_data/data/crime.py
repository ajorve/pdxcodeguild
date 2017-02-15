"""
# Practice: PDX Crime Data

The City of Portland has keeps track of crimes in a publicly available dataset!

Print out a summary of the data:

* The specific most common crime type.
* The rarest crimes.
* The year with the most crime.

### Advanced

Make a jupyter Notebook with a graph of the crime breakdown using `matplotlib`.

"""


import os, sys
import pdb

MEDIA_PREFIX = '/Users/Anders/Desktop/PDX_Code/practice/projects/pdx_crime_data/data/'


def crime_collection():
    file_options = [f for f in os.listdir(MEDIA_PREFIX) if 'csv' in f]
    file = dict(enumerate(file_options))

    print('To find out the list of crimes and occurrence by file, please select from the options', end='\n')
    for opt, name in file.items():
        print(opt, '>>', name)
    print('or', 'q) Quit', sep='\n', end='\n')

    user_selection = int(input('Please make your selection. >> '))

    if user_selection == "":
        sys.exit()

    filename = MEDIA_PREFIX + file[user_selection]
    return filename



def quantify_crime(crime_data):
    crime_counts = dict()

    for crimestr in crime_data[1::]:
        crime = crimestr.split(',')
        offense = crime[3]
        c_data = crime[0:3]
        c_data.append(crime[4])

        try:
            crime_counts[offense].append(c_data)
        except KeyError:
            crime_counts[offense] = list([c_data])

    return crime_counts


def open_file(filename):
    with open(filename) as requested_file:
        text = requested_file.read().replace('"', '')
        return text


def run_program():
    filename = crime_collection()
    text = open_file(filename)
    crimes = [row for row in text.split('\n') if row != '']
    crimes_data = quantify_crime(crimes)
    crimes_counts = {offense: len(c_data) for offense, c_data in crimes_data.items()}

    for offense, count in sorted(crimes_counts.items(), key=lambda t: t[1], reverse=True):
        print(offense, count)

    result = (max(crimes_counts.items(), key= lambda crime: crime[1]))
    print(f"For {filename[-15:]}, {result[0]} has the most incidents with {result[1]}. ")
    return result, crimes_counts

run_program()