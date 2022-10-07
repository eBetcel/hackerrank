#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    altitude = 0
    valley_counter = 0
    is_in_valley = False
    
 
    for move in path:
        if altitude == 0 and move == 'D':
            is_in_valley = True
            
        
        if altitude == -1 and is_in_valley == True and move == 'U':
            is_in_valley = False
            valley_counter += 1
        
        if move == 'D':
            altitude -= 1
        elif move == 'U':
            altitude += 1
            
    return valley_counter
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
