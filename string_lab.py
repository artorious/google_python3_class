#!/usr/bin/env python3
'''Basic string exercises'''

def donuts(count):
    '''Takes one argument <count> (int), where <count> is the number of donuts.
    Returns a string of the form 'Number of donuts: <count>'
    
    If the <count> is 10 or more,
    returns a string of the form 'Number of donuts: Many!'

    Examples:
        donuts(5) >>> 'Number of donuts: 5'
        donuts(25) >>> 'Number of donuts: Many!'
    '''
    return
    
def both_ends(the_string):
    '''Takes one argument <the_string> (str),
    returns a string made of the first 2 and last 2 chars of the original 
    string.

    If the string length is less than 2 chars,
    returns an empty string

    Examples:
        both_ends('spring') >>> 'spng'
        both_ends('spng') >>> 'spng'
        both_ends('tea') >>> 'teea'
        both_ends('a') >>> ''
    '''
    return

def fix_start(the_string):
    '''Takes one argument <the_string> (str),
    returns a string where all occurences of it's first char have been changed
    to '*', except for the first char itself.

    Example:
        fix_start('babble') >>> 'ba**le'
    '''
    return

def mix_up(string_one, string_two):
    '''Takes two arguments <string_one> and <string_two> (str),
    returns a single space separated string '<string_one> <string_two>' with
    the first 2 chars of each string swapped.

    Example:
        mix_up('mix', 'pod') >>> 'pox mid'
        mix_up('dog', 'dinner') >>> 'dig donner'
    
    NOTE: Assume <string_one> and <string_two> are length 2 or more
    '''
    return

def test_sample_data(got, expected):
    '''Takes two arguments <got> and <expected> and performs simple tests 
    for functions used in sample_data()
    where:
        <got> is the function to test (with args)
        <expected> is the expected result
        
    Prints what each function returns vs. what it's suppsed to return
    '''
    pass
          
def sample_data():
    '''Calls functions donuts(), both_ends(), fix_start() and mix_up() with 
    interesting inputs.
    
    Uses test_sample_data() to check if each result is correct or not
    '''
    pass

if __name__ == '__main__':
    sample_data()