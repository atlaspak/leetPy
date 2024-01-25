#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos_count = neg_count = zero_count = 0
    N = len(arr)

    # Calculate counts
    for num in arr:
        if num > 0:
            pos_count += 1
        elif num < 0:
            neg_count += 1
        else:
            zero_count += 1

    # Calculate ratios
    pos_ratio = pos_count / N
    neg_ratio = neg_count / N
    zero_ratio = zero_count / N

    # Print the ratios with 6 digits after the decimal
    print("{:.6f}".format(pos_ratio))
    print("{:.6f}".format(neg_ratio))
    print("{:.6f}".format(zero_ratio))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
