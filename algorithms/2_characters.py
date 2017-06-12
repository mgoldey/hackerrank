#!/bin/python3

import sys

s_len = int(input().strip())
s = input().strip()
def isvalid(t):
  d=[]
  for i in t:
    if i not in d:
      d.append(i)
  if len(d)!=2:
    return False
  for i in range(len(t)-1):
    if t[i]==t[i+1]:
      return False
  return True

def get_all_good_ts(t):
  tl=[]
  d=[]
  for i in t:
    if i not in d:
      d.append(i)
      
  for i in range(len(d)):
    for j in range(len(d)):
      if i==j:
        continue
      test=""
      for k in t:
        if k==d[i] or k==d[j]:
          test+=k
      if isvalid(test):
        tl.append(test)
  if len(tl)==0:
    return 0
  tm=[len(t) for t in tl]      
  return max(tm)
print(get_all_good_ts(s))
      
    

