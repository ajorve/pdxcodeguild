"""
# Phonebook

Make a command line interface phonebook that supports the following options:

__C.R.U.D.__

1. Create New Contact
2. Retrieve Contact
3. Update Existing Contact
4. Delete Contact

Here is an example of contact data being stored with a nickname key as a __dictionary of dictionaries__:

```
phonebook = {'Kieran': {'name': 'Kieran',
                        'number': 8456331959,
                        'phrase': 'Good code is not written, it's re-written.'},
            'Lambda': {'name': 'Lambda',
                         'number': 8454185633,
                         'phrase': 'I am a robot.'}}
```
Here is another implementation; A __list of dictionaries__:

```
phonebook = [{'name': 'Kieran',
            'number':8456331959,
            'phrase': 'Good code is not written, it's re-written.'},
            {'name': 'Lambda',
             'number':8454185633,
             'phrase': 'I am a robot.'}]
```

Or perhaps a __List of lists__:
```
phonebook = [['Kieran',
              8456331959,
              'Good code is not written, it's re-written.'],
              [Lambda',
               8454185633,
               I am a robot.']]
```

###### These are suggestions... Feel free to experiment and store contacts in any way that makes sense to you!

# Advanced
Support searching by:

 - Partial Name
 - Phone Number
 - Partial Phrase

 If there are multiple results, display each of them.


# Super Advanced
- Add Save and Load features for your contact data by saving a csv file.

- Using the python CSV Module's CSVDictReader, download your google contacts and add them to your phonebook on startup


# Future
Use the Twilio API to send a text message from your program.
"""
import sys
import re
from itertools import groupby

# use regex to verify if number is valid format and query info from dictionaries
# use groupby to organize and collect info

PHONEBOOK = {'Kieran': {'name': 'Kieran',
                        'number': 8456331959,
                        'phrase': 'Good code is not written, it\'s re-written.'},
            'Anders': {'name': 'Anders',
                         'number': 8454185633,
                         'phrase': 'I am a robot from the Planet X'}}

def main_menu():
    option = (input("Welcome to Mr. Phonebook, please choose from the Menu Options"
        "\n 1. Create New Contact"
        "\n 2. Retrieve Contact"
        "\n 3. Update Existing Contact"
        "\n 4. Delete Contact"
        "\n 5. Exit Phonebook"
        "\n Please Enter: "))

    if option == '1':
        print("Creating new entry")
        create()

    elif option == '2':
        print("Retrieving entry")
        retrieve()

    elif option == '3':
        print("Updating entry")
        update()

    elif option == '4':
        print("Deleting entry")
        delete()

    elif option == '5':
        print("Exiting Phonebook")
        sys.exit()

def create():
    create_option = input("Would you like to create a new entry? y/n :  ").lower()

    if create_option == 'y':
        create_name = input("Enter the name of the person you would like to add into the phonebook:   ")
        create_number = input("Enter the number of the person you would like to add into the phonebook:   ")
        create_phrase= input("Enter a phrase for the person you would like to add into the phonebook:   ")
        try:


        # creates new entry and returns back to asking the question of create_option

    elif create_option == 'n':
        clear_screen()
        main_menu()
    pass

def retrieve():
    retrieve_option = input("Would you like to retrieve an entry? y/n :  ").lower()

    if retrieve_option == 'y':
        retrieve_dict= input("Insert the name, number, or phrase of the person you are searching for:  ").lower()
        try:
            print("Name: " + PHONEBOOK[retrieve_dict]['name'])
            print("Number: " + PHONEBOOK[retrieve_dict]['phone'])
            print("Phrase: " + PHONEBOOK[retrieve_dict]['phrase'])
        except KeyError:
            print("Entry not found")
        #diplays key and value for dict retrieved. Returns to ask retrieve_option.

    elif retrieve_option == 'n':
        clear_screen()
        main_menu()
    # this function will take user input and use it to search the phonebook
    pass

def update():
    update_option = input("Would you like to update an entry? y/n :  ").lower()

    if update_option == 'y':
        update_name = input("Enter the name for the current phonebook entry:  ")
        print("Do you want to change %s?" % update_name)
        print('y/n? : ')
        updating = True
        while updating:
            try:
                choice = input('> ').lower()
                if choice == 'y' or choice 'yes':
                    PHONEBOOK.append(update_name)

    elif update_option == 'n':
        clear_screen()
        main_menu()
    # this function will take user input and use it to search the phonebook
    pass

def delete():
    delete_option = input("Would you like to update an entry? y/n :  ").lower()

    if delete_option == 'y':
        delete_dict = input("Enter the name, number or phrase for the phonebook entry you want to remove:  ")

    elif delete_option == 'n':
        clear_screen()
        main_menu()
    # this function will take user input and use it to search the phonebook
    pass

def clear_screen():
    print(chr(27) + "[2J")

main_menu()
