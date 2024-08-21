import math
import os
import random
import re
import sys

#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def beautifulTriplets(d, arr):
    # Write your code here
    res=0
    dic={}
    liste=[]
    for i in range(len(arr)):
        if not(arr[i] in dic):
            dic[arr[i]]=1
            liste.append(arr[i])
        else:

            dic[arr[i]]+=1
    for i in range(len(liste)):
        s=1
        s=s*dic[liste[i]]
        if (liste[i]+d) in dic  and  (liste[i]+d+d)in dic:
            s=s*dic[liste[i]+d]
            s=s*dic[liste[i]+d+d]
            res=res+s

    return(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()