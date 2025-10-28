'''Task
Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.'''

#this has to be run in python 2, as hash creation in python generates a random value at each execution, for security improvments, thus the below code wont wokr in python 3

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t=tuple(integer_list)
    print(hash(t))
    
    
#however tried python 3 code is as, implemention of encoder can solve the issue

import hashlib

if __name__ == '__main__':
    n = int(input())
    integer_list = str(map(int, input().split()))
    encded=integer_list.encode('utf-8')
    t=tuple(integer_list)
    hash_obj=hashlib.sha256(encded)
    print(hash_obj)
    print(hash(t))

