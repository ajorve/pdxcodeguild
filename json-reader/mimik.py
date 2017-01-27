'''
Mimic
'''
import sys
from sys import argv
import re
import random
from collections import UserList


def file_open(filename):
    with open(filename, 'r') as file:
        file_text = file.read()
        return file_text
# This opens the file and returns the file text


def scrub(file_text):
    file_scrub = file_text.replace('.', '').replace(',' , '').replace('\n' , ' ')
    scrub_again = re.sub('[&@#$*%()!\d]', '', file_scrub)
    scrubbed = scrub_again.split(" ")
    return scrubbed
# This cleans the file content and returns the cleaned text


def mimic(filename, length=5, slength=5, extra_random=False):
    file_text = file_open(filename)
    scrubbed = scrub(file_text)
    sample_text = dict()

    for current_index, word in enumerate(scrubbed):
        following_words = scrubbed[current_index+1:current_index+length]
        try:
            sample_text[word].extend(following_words)
        except KeyError:
            sample_text[word] = following_words
    # print(sample_text)


    random_keys = random.sample(list(sample_text), slength)
    final_output = list()
    for k in random_keys:
        selection = sample_text[k]
        try:
            word_choice = random.sample(selection, slength)
        except ValueError:
            word_choice = selection

        final_output.extend(word_choice)

    final_output = " ".join(final_output)

    print(k, final_output)
    return final_output

file = sys.argv[1]
mimic(file)
