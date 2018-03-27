#!/bin/python3

import os
import sys

#
# Complete the array2D function below.
#
def array2D(arr):
    #for x in range
    for x in range(len(arr)):
        y=1
    print (len(arr))

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #arr = []
    arr = [[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]

    #for _ in range(6):
   #     arr.append(list(map(int, input().rstrip().split())))

    #print (arr[5][3])
    result = array2D(arr)

    #fptr.write(str(result) + '\n')

    #fptr.close()
