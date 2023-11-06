#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence != '':
        char_one = sentence[0]
    else:
        char_one = None
    return (len(sentence), char_one)
