"""
Fun with Networks

Objective

Write a simple program that accesses a public JSON API and prints the results formatted in a readable way.

1. Create a new file called 'random_users'
2. Fetch JSON representing 5 randomly generated people from the following url 'https://randomuser.me/api/?users=5'
3  Print the results somethings like the following:

Name:
Email:
Username:
Registration:
Birth Date:


"""


# import json
# import requests
# from pprint import pprint as print
#
# def random_users():
#     my_request = requests.get('https://randomuser.me/api/?results=5')
#     people = json.loads(my_request.text)
#
#     for person in people['results']:
#         print('Name: {} {} {}'.format(person['name']['title'], person['name']['first'], person['name']['last']))
#         print('Email: {}'.format(person['email']))
#         print('Username: {}'.format(person['login']['username']))
#         print('Registration: {}'.format(person['registered']))
#         print('Birth Date: {}\n'.format(person['dob']))
#
# random_users()

import json
import requests
from pprint import pprint as pp # pretty print


def random_users():
    my_request = requests.get('https://randomuser.me/api/?results=5')
    people = json.loads(my_request.text)

    for person in people['results']:
        pp('Name: {name[title]} {name[first]} {name[last]}'.format(name = person['name']))
        pp('Email: {}'.format(person['email']))
        pp('Username: {}'.format(person['login']['username']))
        pp('Registration: {}'.format(person['registered']))
        pp('Birth Date: {}\n'.format(person['dob']))

random_users()
