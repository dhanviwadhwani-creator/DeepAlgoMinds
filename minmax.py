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
    # Write your code here
    min_val=arr[0]
    max_val=arr[0]
    sum=0
    for i in range (len(arr)):
       min_val=min(min_val,(arr[i]))
       max_val=max(max_val,(arr[i]))
       sum=sum+arr[i]
    print(sum-max_val,sum-min_val)
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
