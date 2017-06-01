n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
nswaps=0
def swap(b,i,j):
  k=b[i]
  b[i]=b[j]
  b[j]=k
  return b
for i in range(n):
  for j in range(i+1,n,1):
    if a[j]<a[i]:
      nswaps+=1
      a=swap(a,i,j)
print("Array is sorted in {:} swaps.\nFirst Element: {:}\nLast Element: {:}".format(nswaps,a[0],a[-1]))
