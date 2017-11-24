#!/usr/bin/env python3
'''Basic List exercises'''

def match_ends(words):
    '''Takes a list of strings, <words>

    Returns the count of the number of strings where the string length is 2 or 
    more and the first and last chars of the string are the same.
    '''
    count = 0
    for str_item in words:
        if isinstance(str_item, str):
            str_item = str_item.strip()
            if len(str_item) > 1 and str_item[0] == str_item[-1]:
                count += 1
        else:
            return 'Expected a list of strings Exclusively'       
    return count
 

def front_x(words):
    '''Takes a list of strings, <words>
    Returns a list with the strings in sorted order, except all the strings 
    that begin with 'x' are group first.

    Example:
        ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] >>> ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    '''
# Hint: this can be done by making 2 lists and sorting each of them before combining them.
    return

def sort_last(tuples):
    '''Takes a list of non-empty tuples, <tuples>

    Returns a list sorted in increasing order by the last element in each tuple.

    Example:
        [(1, 7), (1, 3), (3, 4, 5), (2, 2)] >>> [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    '''
# Hint: use a custom key= function to extract the last element form each tuple.
    return

def remove_adjacent(nums):
    '''Takes a list of numbers (int), <nums>.

    Returns a list where all adjacent == elements have been reduced to a single element.  

    Example:
        [1, 2, 2, 3] >>> [1, 2, 3].
    '''
    return

def linear_merge(list1, list2):
    '''Takes two lists, <list1> and <list2> sorted in increasing order,
    creates a merged list of all the elements in sorted order.

    Returns the merged list
    '''
# Ideally, the solution should work in "linear" time, making a single pass of both lists.
# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.
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
        prefix = ' PASSED '
    else:
        prefix = '  FAILED '
    print('{0} got: {1} expected: {2}'.format(prefix, repr(got), repr(expected)))



def sample_data():
    '''Calls functions match_ends(), front_x(), sort_last(), remove_adjacent()
    and linear_merge with interesting inputs.
    
    Uses test_sample_data() to check result against expected output
    '''
    print(format(' match_ends ', '*^60'))
    test_sample_data(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test_sample_data(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test_sample_data(match_ends(['aaa', 'be', 'abc', 'hello']), 1)
    test_sample_data(match_ends([' aaa', 'be  ', 'abc', '     hello']), 1) # test whitespace handling
    test_sample_data(match_ends(['    ', '          ' ]), 0)
    test_sample_data(match_ends(['aaa', 1, 'abc', 'hello']), 
        'Expected a list of strings Exclusively') # Test handlindling of non-string item on list
    test_sample_data(match_ends(['aaa', ['aaa'], 'abc', 'hello']), 
    'Expected a list of strings Exclusively')
    test_sample_data(match_ends(['aaa', ('aaa', 'aaa'), 'abc', 'hello']), 
    'Expected a list of strings Exclusively')
    test_sample_data(match_ends([[1,2,3,1], ['aaa'], 'abc', 'hello']), 
    'Expected a list of strings Exclusively')

    print()
    print(format(' front_x ', '*^60'))
    test_sample_data(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
        ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test_sample_data(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
        ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test_sample_data(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
        ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

       
    print()
    print(format(' sort_last ', '*^60'))
    test_sample_data(sort_last([(1, 3), (3, 2), (2, 1)]),
        [(2, 1), (3, 2), (1, 3)])
    test_sample_data(sort_last([(2, 3), (1, 2), (3, 1)]),
        [(3, 1), (1, 2), (2, 3)])
    test_sample_data(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
        [(2, 2), (1, 3), (3, 4, 5), (1, 7)])

if __name__ == '__main__':
    sample_data()
    
