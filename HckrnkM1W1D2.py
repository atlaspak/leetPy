#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    min = sys.maxsize
    max = 0
    total = 0
    
    for num in arr:
        if num > max:
            max = num
        if num < min:
            min = num
        total += num
        
    print("{} {}".format((total - max), (total - min)))
            
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
