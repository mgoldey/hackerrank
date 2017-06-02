#!/bin/python3

import sys
def numberOfLists(s, m, d):
    # Complete this function
    # m is max of numbers
    a=[i for i in range(1,min(m,s)+1,1)] # GUESS VALUES HERE
    la=len(a)
    # d is max change between numbers
    # s is sum of array      
    res=[[0 for j in range(la+1)] for i in range(s+1)] # TABLE FOR ANSWERS
    res[0][0]=1 # ONLY ONE WAY TO GET NOTHING
    for j in range(1,la+1,1):
      res[0][j]=1
    for i in range(0,s+1,1):
      for j in range(1,la+1,1):
        s=a[j-1]
        if ((i-s)>=0):
          res[i][j]=res[i-s][la]+res[i][j-1]
        else:
          res[i][j]=res[i][j-1]
    print(res)
    return res[-1][-1]%(10**9+9)
    

#  Return the number of lists satisfying the conditions above, modulo 1000000009.
s, m, d = input().strip().split(' ')
s, m, d = [int(s), int(m), int(d)]
result = numberOfLists(s, m, d)
print(result)

