#!/usr/bin/python3
def islower(c):
    for char in range(97, 123):
        if c in chr(char):
            return True
    return False
