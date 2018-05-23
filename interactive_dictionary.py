# !/usr/local/bin/python
# encoding: utf-8
"""
    File name:
    Author: LeeKLTW
    Date created: 05/22/2018
    Date last modified: 05/23/2018
    Python Version: 3.5.3
"""
import json
from difflib import get_close_matches
data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data))>0:
        response = input('Did you mean %s ?(Y/N)' % get_close_matches(word,data)[0])
        if response.lower() == 'y':
            return data[get_close_matches(word,data)[0]]
        else:
            return 'Please enter the word again.'
    else:
        return "The word doesn't exist, please double check it."
def display(output):
    if type(output) == list:
        for i in zip(range(len(output)),output):
            print(i[0]+1,'.',i[1])
    else:
        print(output)

word = input('Enter a word, enter "x" to exit:')
while True:
    if word == 'x':
        print('Good bye!')
        break
    else:
        display(translate(word))
        word = input('Enter a word, enter "x" to exit:')
