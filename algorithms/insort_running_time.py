n=int(input())
a=[int(i) for i in input().split()]
res=[a[0]]
def p(a):
  print(" ".join(str(i) for i in a))
c=0
def insert(a,i):
  global c
  """ for index i, find correct position in a """
  k=a[i]
  la=len(a)
  j=i-1
  while j>=0:
    if a[j]>k:
      a[i]=a[j]
      c+=1
    else:
      break
    i-=1
    j-=1
  a[i]=k
  return
for i in range(1,n):
  insert(a,i)
print(c)

