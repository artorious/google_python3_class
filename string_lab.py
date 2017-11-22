#!/usr/bin/env python3
'''Basic string exercises'''

def donuts(count):
    '''Takes one int argument <count>, the number of donuts.
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
    '''Takes one str argument <the_string> ,
    returns a string made of the first 2 and last 2 alpha-numeric chars of the original 
    string.

    If the string length is less than 2 alpha-numeric chars,
    returns an empty string

    Examples:
        both_ends('spring') >>> 'spng'
        both_ends('spng') >>> 'spng'
        both_ends('tea') >>> 'teea'
        both_ends('a') >>> ''
    '''
    if isinstance(the_string, str):
        if len(the_string.strip()) > 1: # Check for alpha-numeric chars excluding leading & trailing whitespace
            the_string = the_string.strip() # strip off leading & trailing whitespace and assign
            first_two_chars = the_string[:2]
            last_two_chars = the_string[-2:]
            return first_two_chars + last_two_chars
        else:
            return ''
    else:
        return 'Expected string'

def fix_start(the_string):
    '''Takes one str argument <the_string> ,
    returns a string where all occurences of it's first alpha-numeric char have 
    been changed to '*', except for the first alpha-numeric char itself.

    Example:
        fix_start('babble') >>> 'ba**le'
    '''
    if isinstance(the_string, str) :
        if len(the_string.strip()) > 1: # Check for alpha-numeric chars excluding leading & trailing whitespace
            the_string = the_string.strip() # strip off leading & trailing whitespace and assign
            first_char = the_string[0] # Set first char aside
            play_str = the_string[1:] # assign the rest of the string 
            return first_char + play_str.replace(first_char, '*')
        else:
            return the_string.strip()
    else:
        return 'Expected string'

def mix_up(string_one, string_two):
    '''Takes two str arguments <string_one> and <string_two> ,
    returns a single space separated string '<string_one> <string_two>' with
    the first 2 alpha-numeric chars of each string swapped.

    Example:
        mix_up('mix', 'pod') >>> 'pox mid'
        mix_up('dog', 'dinner') >>> 'dig donner'
    
    '''
    
    if isinstance(string_one, str) and isinstance(string_two, str):
        if len(string_one.strip()) > 2 and len(string_two.strip()) > 2:
            string_one, string_two = string_one.strip(), string_two.strip() # Strip lead & trailing whitespace
            string_one_swaped = string_two[:2] + string_one[2:]
            string_two_swaped = string_one[:2] + string_two[2:]
            return '{0} {1}'.format(string_one_swaped, string_two_swaped)
        else:
            return 'Expected strings with at least 3 alpha-numeric chars'
    else:
        return 'Expected string'

def verbings(the_string):
    '''Takes one str argument <the_string>, if it's length is at least 3 
    alpha-numeric chars, adds 'ing' to it's end. Unless it already ends in 
    'ing', in which case adds 'ly' instead. If <the_string> length is less 
    than 3 alpha-numeric chars, it's left unchanged.

    Returns the resulting string.
    '''
    if isinstance(the_string, str):
        the_string = the_string.strip()
        if len(the_string) > 2:
            if the_string.endswith('ing'):
                return '{0}ly'.format(the_string)
            else:
                return '{0}ing'.format(the_string) 
        else:
            return the_string
    else:
        return 'Expected string'

def not_bad(the_string):
    '''Takes one str argument <the_string>, finds the first appearance of the
    substring 'not' and 'bad'. If the 'bad' follows the 'not', replaces the 
    whole 'not'...'bad' substring with 'good'.

    Returns the resulting string.
    Example:
        not_bad('This dinner is not that bad!') >>> 'This dinner is good!'
    '''
    # TODO: Look into module re for regular expressions
    # use pattern searching to make function more robust and handle failing tests
    if isinstance(the_string, str) :
        the_string = the_string.strip()
        
        if the_string != '':
            not_indx, bad_indx = the_string.find('not'), the_string.find('bad')
            if not_indx != -1 and bad_indx != -1 and bad_indx > not_indx:
                new_string = the_string[:not_indx] + 'good' + \
                                the_string[bad_indx + 3: ]
                return new_string
            else:
                return the_string    
        else:
            return the_string
    else:
        return 'Expected string'

def front_back(string_one, string_two):
    '''Takes two str arguments <string_one> and <string_two>, for each 
    alpha-numeric string, divide into two halves. If the length is even(The 
    front and back halves are the same length.). If the length is odd, the 
    extra char goes in the front half. E.g. 'abcde', the front half is 'abc', 
    the back half 'de'.
    
    Returns a string of the form, 
        string_one-front + string_two-front + string_one-back + string_two-back
    '''
    if isinstance(string_one, str) and isinstance(string_two, str):
        string_one, string_two = string_one.strip(), string_two.strip()
        if len(string_one) < 2 or len(string_two) < 2:
            return string_one + string_two
        else: # Determine mid position for each string
            s_one_mid = len(string_one) // 2
            s_two_mid = len(string_two) // 2
            # Add 1 if length is odd
            if len(string_one) % 2 == 1: 
                s_one_mid += 1
            if len(string_two) % 2 == 1:
                s_two_mid += 1
            # Output
            return string_one[ :s_one_mid] + string_two[ :s_two_mid] + \
                    string_one[s_one_mid: ] + string_two[s_two_mid: ]


            
    else:
        return 'Expected strings'


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
    print('{0} got: {1}  --> expected: {2}'.format(result, repr(got), 
        repr(expected)))
          
def sample_data():
    '''Calls functions donuts(), both_ends(), fix_start(), mix_up() verbings(), 
    not_bad() and front_back() with interesting inputs.
    
    Uses test_sample_data() to check result against expected output
    '''
    print(format(' Test Donut() ', '*^60'))
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
    print(format(' Test both_ends() ', '*^60'))
    test_sample_data(both_ends('spring'), 'spng')
    test_sample_data(both_ends('hello'), 'helo')
    test_sample_data(both_ends('a'), '')
    test_sample_data(both_ends('   a   '), '')
    test_sample_data(both_ends('an'), 'anan')
    test_sample_data(both_ends('   an    '), 'anan')
    test_sample_data(both_ends('            '), '')
    test_sample_data(both_ends(''), '')
    test_sample_data(both_ends('xyz'), 'xyyz')
    test_sample_data(both_ends(1), 'Expected string')
    test_sample_data(both_ends((1,)), 'Expected string')
    test_sample_data(both_ends(1.5), 'Expected string')
    test_sample_data(both_ends(['1']), 'Expected string')

    print()
    print(format(' Test fix_start() ', '*^60'))
    test_sample_data(fix_start('babble'), 'ba**le')
    test_sample_data(fix_start('aadvark'), 'a*dv*rk')
    test_sample_data(fix_start('google'), 'goo*le')
    test_sample_data(fix_start('donut'), 'donut')
    test_sample_data(fix_start('   donuts   '), 'donuts')
    test_sample_data(fix_start('     '), '')
    test_sample_data(fix_start(''), '')
    test_sample_data(fix_start('a'), 'a')
    test_sample_data(fix_start(1), 'Expected string')
    test_sample_data(fix_start((1,)), 'Expected string')
    test_sample_data(fix_start(1.5), 'Expected string')
    test_sample_data(fix_start(['1']), 'Expected string')

    print()
    print(format(' Test mix_up() ', '*^60'))
    test_sample_data(mix_up('mix', 'pod'), 'pox mid' )
    test_sample_data(mix_up('dog', 'dinner'), 'dig donner' )
    test_sample_data(mix_up('gnash', 'sport'), 'spash gnort' )
    test_sample_data(mix_up('pezzy', 'firm'), 'fizzy perm' )
    test_sample_data(mix_up('  mix', 'pod  '), 'pox mid' )
    test_sample_data(mix_up('mix', '  pod'), 'pox mid' )
    test_sample_data(mix_up('a', 'b'), 'Expected strings with at least 3 alpha-numeric chars' )
    test_sample_data(mix_up('ab', 'ba'), 'Expected strings with at least 3 alpha-numeric chars' )
    test_sample_data(mix_up('ab', 'ba'), 'Expected strings with at least 3 alpha-numeric chars' )
    test_sample_data(mix_up('ab   ', '    ba'), 'Expected strings with at least 3 alpha-numeric chars' )
    test_sample_data(mix_up('abc   ', '    ba'), 'Expected strings with at least 3 alpha-numeric chars' )
    test_sample_data(mix_up('', ''), 'Expected strings with at least 3 alpha-numeric chars' )
    test_sample_data(mix_up('      ', ' '), 'Expected strings with at least 3 alpha-numeric chars')
    test_sample_data(mix_up(1, ''), 'Expected string' )
    test_sample_data(mix_up('', 1.5), 'Expected string' )
    test_sample_data(mix_up([1], ''), 'Expected string' )
    test_sample_data(mix_up('', (1,2)), 'Expected string' )
    
    print()
    print(format(' Test verbing() ', '*^60'))
    test_sample_data(verbings('hail'), 'hailing')
    test_sample_data(verbings('  hail   '), 'hailing')
    test_sample_data(verbings('swiming'), 'swimingly')
    test_sample_data(verbings('  swiming   '), 'swimingly')
    test_sample_data(verbings('do'), 'do')
    test_sample_data(verbings('  do   '), 'do')
    test_sample_data(verbings(''), '')
    test_sample_data(verbings('      '), '')
    test_sample_data(verbings(1), 'Expected string')
    test_sample_data(verbings(1.5), 'Expected string')
    test_sample_data(verbings([1.5]), 'Expected string')

    print()
    print(format(' Test not_bad() ', '*^60'))
    test_sample_data(not_bad('This movie is not so bad'), 'This movie is good')
    test_sample_data(not_bad('This movie is nothing else but bad'), 'This movie is nothing else but bad')
    test_sample_data(not_bad('This movie is nothing but the  baddest film'), 'This movie is nothing but the  baddest film')
    test_sample_data(not_bad('This movie is not the baddest film'), 'This movie is not the baddest film')
    test_sample_data(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test_sample_data(not_bad('This thing has me in a knot thats bad!'), 'This thing has me in a knot thats bad!')
    test_sample_data(not_bad('This thing is not, as bad!'), 'This thing is good!')
    test_sample_data(not_bad('This tea is not hot'), 'This tea is not hot')
    test_sample_data(not_bad("It's bad yet not"), "It's bad yet not")
    test_sample_data(not_bad(''), '')
    test_sample_data(not_bad('        '), '')
    test_sample_data(not_bad(1), 'Expected string')
    test_sample_data(not_bad(1.5), 'Expected string')
    test_sample_data(not_bad(['a']), 'Expected string')

    print()
    print(format(' Test front_back() ', '*^60'))
    test_sample_data(front_back('abcd', 'xy'), 'abxcdy')
    test_sample_data(front_back('   abcd', 'xy      '), 'abxcdy')
    test_sample_data(front_back('  abcd', 'xy     '), 'abxcdy')
    test_sample_data(front_back('abcd', '' ), 'abcd')
    test_sample_data(front_back('', 'abcd' ), 'abcd')
    test_sample_data(front_back('abcde', 'xyz'), 'abcxydez')
    test_sample_data(front_back('Kitten', 'Donut'), 'KitDontenut')
    test_sample_data(front_back('   ', '   '), '')
    test_sample_data(front_back('', ''), '')
    test_sample_data(front_back('abcd', 12 ), 'Expected strings')
    test_sample_data(front_back(12, 'abcd' ), 'Expected strings')
    test_sample_data(front_back([12], 'abcd' ), 'Expected strings')
    


if __name__ == '__main__':
    sample_data()