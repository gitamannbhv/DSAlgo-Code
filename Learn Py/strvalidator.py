'''Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.
In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.'''

if __name__ == '__main__':
    s = input()

    has_alnum = any(c.isalnum() for c in s)
    has_alpha = any(c.isalpha() for c in s)
    has_digit = any(c.isdigit() for c in s)
    has_lower = any(c.islower() for c in s)
    has_upper = any(c.isupper() for c in s)

    if has_alnum:
        print(True)
    else:
        print(False)

    if has_alpha:
        print(True)
    else:
        print(False)

    if has_digit:
        print(True)
    else:
        print(False)

    if has_lower:
        print(True)
    else:
        print(False)

    if has_upper:
        print(True)
    else:
        print(False)