#!/bin/python3

import sys


arr = []
for arr_i in range(6):
  arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
  arr.append(arr_t)

m=-9*7
hs=[[0 for i in range(6)] for j in range(6)]
for i in range(1,5,1):
  for j in range(1,5,1):
    hs[i][j]+=arr[i][j]
    hs[i][j]+=arr[(i-1)%6][(j-1)%6]
    hs[i][j]+=arr[(i-1)%6][(j)%6]
    hs[i][j]+=arr[(i-1)%6][(j+1)%6]
    hs[i][j]+=arr[(i+1)%6][(j-1)%6]
    hs[i][j]+=arr[(i+1)%6][(j)%6]
    hs[i][j]+=arr[(i+1)%6][(j+1)%6]
    if hs[i][j]>m:
      m=hs[i][j]
print(m)
    
    


