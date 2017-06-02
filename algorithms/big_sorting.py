n=int(input())
a=[]
l=[]
for i in range(n):
  j=input()
  lj=len(j)
  a.append(j)
  l.append(lj)# Store lengths to enable sorting in different buckets
b=zip(l,a) # store lengths and vals
for j in sorted(b):
  print(j[1])
