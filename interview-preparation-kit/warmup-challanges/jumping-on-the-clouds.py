#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    index = 0
    steps = 0
    while (index < len(c) -1):
        if index == len(c) - 2:
            index += 1
            steps += 1
            return steps
        
        elif c[index + 2] == 0:
            steps += 1
            index += 2
        elif c[index + 1] == 0:
            steps += 1
            index += 1
        
    return steps           

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
