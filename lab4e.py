#!/usr/bin/env python3
# Author ID: btaylor31


def is_digits(sobj):
    # place code here - loop through each character in sobj
    tmp_boolean = True
    all_digits = '0123456789' # setting value for digits
    for char in sobj:
        if char in all_digits:
            tmp_boolean = True
        else:
            tmp_boolean = False
            return tmp_boolean

    return tmp_boolean # provides return value

if __name__ == '__main__': # main code block
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')
