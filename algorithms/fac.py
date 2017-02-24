#!/bin/python3

import sys


n = int(input().strip())
def fac(i):
  if i==1:
    return 1
  if i==0:
    return 1
  return i*fac(i-1)

print(fac(n))
