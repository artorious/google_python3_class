#!/usr/bin/env python3
'''Test python3 installation
A tiny python program that checks that python3 is working.
Usage:
    python3 hello.py
    python3 hello.py Arthur
    python3 hello.py "Arthur Ngondo"
    python3 hello.py Arthur\ Ngondo
Output:
    Hello World -or- Hello Arthur -or- Hello Arthur Ngondo

NOTE: Escape spaces or "Quote commad line Arguments containing spaces"
'''
__AUTHOR__ = 'Nick Parlante'
__CONTRIBUTOR__ = 'Arthur Ngondo'

import sys

def hello():
    '''Prints default greeting, "Hello World" 
    If script is passed a command line argument,
    prints "Hello <argument>"
    '''
    if len(sys.argv) >= 2: # Check for commadline arg
        name = sys.argv[1]
    else:
        name = 'World!' # Fallback
    
    print('Hello there {0}'.format(name))

if __name__ == '__main__':
    hello()                                                                           