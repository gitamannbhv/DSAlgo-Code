'''Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird'''

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2!=0 and 1<= n <=100:
        print("Weird")
    else:
        if 2<= n <=5:
            print("Not Weird")
        elif 6<= n <=20:
            print("Weird")
        elif 20<= n <=100:
            print("Not Weird")
        else:
            print("enter num btw 1 to 100")
