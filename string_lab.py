#!/usr/bin/env python3
'''Basic string exercises'''

def donuts(count):
    '''Takes one argument <count>, where <count> is the number of donuts.
    Returns a string of the form 'Number of donuts: <count>'
    
    If the <count> is 10 or more,
    returns a string of the form 'Number of donuts: Many!'

    Examples:
        donuts(5) >>> 'Number of donuts: 5'
        donuts(25) >>> 'Number of donuts: Many!'
    '''

    try: # Check if  <count> is int
        if count >= 0 and count < 10:
            return 'Number of donuts: {0}'.format(str(count))
        elif count < 0:
            return 'None'
        else:
            return 'Number of donuts: Many!'
    except TypeError:
        return 'Expected integer'
     
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
    if isinstance(the_string, str):
        if len(the_string) > 1:
            first_two_chars = the_string[:2]
            last_two_chars = the_string[-2:]
            return first_two_chars + last_two_chars
        else:
            return ''
    else:
        return 'Expected string'

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
    if got == expected:
        result = 'PASSED'
    else:
        result = 'FAILED'
    print('{0} got: {1}  but expected: {2}'.format(result, repr(got), 
        repr(expected)))
          
def sample_data():
    '''Calls functions donuts(), both_ends(), fix_start() and mix_up() with 
    interesting inputs.
    
    Uses test_sample_data() to check result against expected output
    '''
    print(format(' Test Donut Count ', '*^60'))
    test_sample_data(donuts(4), 'Number of donuts: 4' )
    test_sample_data(donuts(9), 'Number of donuts: 9' )
    test_sample_data(donuts(10), 'Number of donuts: Many!' )
    test_sample_data(donuts(19), 'Number of donuts: Many!' )
    test_sample_data(donuts('one'), 'Expected integer' )
    test_sample_data(donuts(1.5), 'Number of donuts: 1.5' )
    test_sample_data(donuts(-1), 'None')
    test_sample_data(donuts(0), 'Number of donuts: 0' )
    test_sample_data(donuts([1,2]), 'Expected integer' )
    
    print()
    print(format(' Test both_ends ', '*^60'))
    test_sample_data(both_ends('spring'), 'spng')
    test_sample_data(both_ends('hello'), 'helo')
    test_sample_data(both_ends('a'), '')
    test_sample_data(both_ends('an'), 'anan')
    test_sample_data(both_ends(''), '')
    test_sample_data(both_ends('xyz'), 'xyyz')
    test_sample_data(both_ends(1), 'Expected string')
    test_sample_data(both_ends((1,)), 'Expected string')
    test_sample_data(both_ends(1.5), 'Expected string')
    test_sample_data(both_ends(['1']), 'Expected string')

    print()
    print(format(' Test fix_start ', '*^60'))
    test_sample_data(fix_start('babble'), 'ba**le')
    test_sample_data(fix_start('aadvark'), 'a*dv*rk')
    test_sample_data(fix_start('google'), 'goo*le')
    test_sample_data(fix_start('donut'), 'donut')

    print()
    print(format(' Test mix_up ', '*^60'))
    test_sample_data(mix_up('mix', 'pod'), 'pox mid' )
    test_sample_data(mix_up('dog', 'dinner'), 'dig donner' )
    test_sample_data(mix_up('gnash', 'sport'), 'spash gnort' )
    test_sample_data(mix_up('pezzy', 'firm'), 'fizzy perm' )

if __name__ == '__main__':
    sample_data()