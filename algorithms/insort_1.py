n=int(input())
a=[int(i) for i in input().strip().split()]
la=len(a)
i=la-2
j=-1
k=a[j]
while i>=0:
  if a[i]>k:
    a[j]=a[i]
  else:    
    break
  j-=1
  i-=1
  print(" ".join(str(l) for l in a))
a[j]=k

print(" ".join(str(l) for l in a))


