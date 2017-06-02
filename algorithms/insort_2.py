n=int(input())
a=[int(i) for i in input().split()]
res=[a[0]]
def p(a):
  print(" ".join(str(i) for i in a))
  
def insert(a,i):
  """ for index i, find correct position in a """
  k=a[i]
  la=len(a)
  j=i-1
  while j>=0:
    if a[j]>k:
      a[i]=a[j]
    else:
      break
    i-=1
    j-=1
  a[i]=k
  return
for i in range(1,n):
  insert(a,i)
  p(a)

  
