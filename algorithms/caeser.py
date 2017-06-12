#!/bin/python3

import sys


n = int(input().strip())
s = input().strip()
k = int(input().strip())
alpha_upper=list("abcdefghijklmnopqrstuvwxyz".upper())
alpha_lower=list("abcdefghijklmnopqrstuvwxyz")
inds=[i for i in range(52)]
d={}
for i in range(26):
  d[alpha_upper[i]]=str(i)
  d[alpha_lower[i]]=str(i+26)
  d[i]=alpha_upper[i]
  d[i+26]=alpha_lower[i]
d['-']='-'

def caeser(t,k):
  res=""
  for i in t:
    try:
      j=d[i]
      j=int(j)
      if j<26:
        res+=d[(j+k)%26]
      else:
        res+=d[26+(j+k)%26]
    except:
      res+=i
  return res
print(caeser(s,k))
