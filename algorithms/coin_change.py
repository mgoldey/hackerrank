#!/bin/python3

import sys

def getWays(n, c):
    lc=len(c)
    res=[[0 for i in range(lc+1)]for j in range(n+1)]
    res[0][0]=1
    for i in range(1,lc+1):
      res[0][i]=1
    for i in range(1,n+1,1):
      for j in range(1,lc+1,1):
        res[i][j]=res[i][j-1]
        s=c[j-1]
        if (i-s)>=0:
          res[i][j]+=res[i-s][j]
    #print(res)
    return res[-1][-1]

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
print(ways)

