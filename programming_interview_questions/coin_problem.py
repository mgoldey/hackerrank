#!/bin/python3
# COUNT NUMBER OF WAYS TO MAKE CHANGE FOR A GIVEN SET OF COIN VALUES AND A VALUE - USING DYNAMIC PROGRAMMING TO STORE RESULTS
import sys
from collections import defaultdict
def getWays(n, c):
  # Complete this function
  lc=len(c)
  res=[[0 for i in range(n+1)] for j in range(lc+1)] 
  res[0][0]=1
  for j in range(1,lc+1,1):
    res[j][0]=1
  for i in range(0,n+1,1):
    for j in range(1,lc+1,1):
      if (i-c[j-1])>=0:
        res[j][i]=res[j][i-c[j-1]]+res[j-1][i]
      else:
        res[j][i]=res[j-1][i]      
  return res[-1][-1]
       
n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
print(ways)
