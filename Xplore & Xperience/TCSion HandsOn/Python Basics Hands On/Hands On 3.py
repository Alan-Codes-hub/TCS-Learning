#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'checkCoPrimeExistance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY numbers as parameter.
#

def checkCoPrimeExistance(numbers):
    c=0
    for i in numbers:
        temp=0
        if(i==0 or i==1):
            temp=1
        for j in range(2,i):
            if(i%j==0):
                temp=1
                break
        if(temp!=1):
            c+=1
    return c
