#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        b = None
    else:
        a, b = len(sentence), sentence[0]
    return a, b
