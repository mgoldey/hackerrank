# Enter your code here. Read input from STDIN. Print output to STDOUT

#SOLVE BY USING SUB PROBLEMS AND DYNAMIC PROGRAMMING
from math import floor
x=int(input())
n=int(input())
ix=floor(x**(1/n))
vals=[i**n for i in range(1,ix+1)]
lv=len(vals)
res=[0 for j in range(x+1)]
res[0]=1
for i in range(lv):
  v=vals[i]
  for j in range(x,v-1,-1):
    res[j]+=res[j-v]
print(res[-1])
