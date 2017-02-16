
a = input().strip()
b = input().strip()

from copy import deepcopy
ad={}
bd={}
for i in a:
  if i in ad.keys():
    ad[i]=ad[i]+1
  else:
    ad[i]=1
for i in b:
  if i in bd.keys():
    bd[i]=bd[i]+1
  else:
    bd[i]=1
bad=0
cd=[i for i in ad.keys()]
for i in cd:
  if i in bd.keys():
    j=ad.pop(i)
    k=bd.pop(i)
    if (j>k):
      bad+=(j-k)
    elif(k>j):
      bad+=(k-j)
for j in ad.keys():
  bad+=ad[j]      
for j in bd.keys():
  bad+=bd[j]
    

print(bad)

