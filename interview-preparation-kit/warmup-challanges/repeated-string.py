#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#


def repeatedString(s, n):
    # Write your code here
   
    occurrences_one_word = 0
    for i in s:
        if i == 'a':
            occurrences_one_word += 1
    
    result = n // len(s) * occurrences_one_word
    
    last_counter = n % len(s)
    for i in range(last_counter):
        if s[i] == 'a':
            result += 1
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
