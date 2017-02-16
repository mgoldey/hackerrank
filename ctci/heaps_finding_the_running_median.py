#!/bin/python3

import sys
import bisect
import math

n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
    a_t = int(input().strip())
    bisect.insort_left(a,a_t)
    la=len(a)
    if (la%2==1):
      print("{:.1f}".format(a[la//2]))
    else:
      lm1=int(math.floor(la/2))-1
      lm2=lm1+1
      print("{:.1f}".format(0.5*a[lm1]+.5*a[lm2]))
    

