#!/bin/python3

import sys
s = input().strip()
t = input().strip()
k = int(input().strip())
ls=len(s)
lt=len(t)
lm=min(ls,lt)

matching=0
for i in range(lm):
  if s[i]==t[i]:
    matching+=1
  else:
    break
ops=ls+lt-2*matching
if k==ops:
  print("Yes")
elif (k>ops):
  if (k-ops)%2==0:
    print("Yes")
  else:
      if ls<lt:
        k=k-ls
        if k>lt:
          print("Yes")
        else:
          print("No")
      else:
        k=k-lt
        if k>ls:
          print("Yes")
        else:
          print("No")
else:
  print("No")
