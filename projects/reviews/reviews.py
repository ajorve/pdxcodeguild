"""
# Practice: Reviews

Save your solution as `practice/reviews.py`.

We're going to model a mini version of [Yelp](http://www.yelp.com/).
There are local business listings and users can post reviews, with a rating (1 - 5 points) and some text, of each business.

Write a program that will read a database of businesses, users, and reviews.

Businesses have:

* A name
* A location city

Users have:

* A name
* A hometown

Reviews have:

* The user name that wrote it
* The business name it is about
* A rating
* Some description text

Load in this data encoded in JSON format from these files.
Each line in these files is a single object of that kind.

* [Business Data](./reviews-businesses.txt)
* [User Data](./reviews-users.txt)
* [Review Data](./reviews-reviews.txt)


"""


import re
import sys
import os
import json
import requests
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator


def menu():
    user_selection = int(input('Please make your selection.\n '
                           'Search By 1.Business Name, 2.Address, or 3.Phone Number: >  '))

    if user_selection == 1:
        name = input("Please enter the Business Name to search by:  ")
        return name

    elif user_selection == 2:
        address = input("Please enter the Address to search by:  ")
        return address

    elif user_selection == 3:
        phone = input("Please enter the Phone Number to search by:  ")
        return phone

    elif user_selection == "":
        print("Exiting Program")
        sys.exit()


def display_info(api_url, api_key):

    info = json.loads(api_url, api_key)

    for name in info['results']:
        print(f'Name: {name[title]} {name[first]} {name[last]}')
        print(f'Email: {email}')
        print(f'Business: {business}')
        print(f'Location: {location}')
        print(f'Established: {established}\n')


def data_collection(url):
    query = data_filtering(**params)
    api_url = requests.get('https://api.yelp.com/v2/search/')
    url_query = api_url + creds + query
    # read API keys
    with io.open('config_secret.json') as cred:
        creds = json.load(cred)
        auth = Oauth1Authenticator(**creds)
        client = Client(auth)

    return client


def data_extraction():
    # clean and format the data



def data_filtering(client, **params):

    if menu() == 1:
        search_by_business_name = client.get_business(**params)
        return search_by_business_name

    elif menu() == 2:
        search_by_business_address = client.search(**params)
        return search_by_business_address

    elif menu() == 3:
        search_by_business_phone = client.phone_search(**params)
        return search_by_business_phone
