#!/bin/python3

import sys

def lonely_integer(a):
    d={}
    for i in a:
      d[i]=0
    for i in a:
      d[i]+=1
    for j in d.keys():
      if d[j]==1:
        return j

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))

