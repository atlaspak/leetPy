#!/bin/python3

import math
import os
import random
import re
import sys
import datetime

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hours, minutes, seconds = map(int, s[:-2].split(':'))
    period = s[-2:]
    
    if period == "PM" and hours < 12:
        hours += 12
    elif period == "AM" and hours == 12:
        hours = 0
        
    return "{:02}:{:02}:{:02}".format(hours, minutes, seconds)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
