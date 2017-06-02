#!/bin/python3

import sys

def t(x1,x0,v):
  d=abs(x1-x0)
  return d/v
def whoGetsTheCatch(n, x, X, V):
    # Complete this function
    lx=len(X)
    ts=[t(X[i],x,V[i]) for i in range(lx)]
    if lx==0:
      return -1
    if lx==1:
      return 0
    res=sorted(zip(ts,range(lx)))
    if res[0][0]==res[1][0]:
      return -1
    else:
      return res[0][1]
    
      
#  Return the index of the catcher who gets the catch, or -1 if no one gets the catch.
n, x = input().strip().split(' ')
n, x = [int(n), int(x)]
X = list(map(int, input().strip().split(' ')))
V = list(map(int, input().strip().split(' ')))
result = whoGetsTheCatch(n, x, X, V)
print(result)

