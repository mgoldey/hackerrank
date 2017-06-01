# MUST BE SUBMITTED USING PYPY
def count_inversions(a):
  def swap(b,i,j):
    k=b[i]
    b[i]=b[j]
    b[j]=k
    return b
    
  def merge_sort(m):
    nswaps=0
    lm=len(m)
    if lm<=1:
      return 0
    lm2=lm//2
    l=m[:lm2]
    r=m[lm2:]
    nswaps+=merge_sort(l)
    nswaps+=merge_sort(r)

    ll=len(l)
    lr=len(r)
    i,j,k=0,0,0
    while i<ll and j<lr:
      if r[j]<l[i]:
        nswaps+=ll-i
        m[k]=r[j]
        j+=1
      else:      
        m[k]=l[i]
        i+=1
      k=k+1
    while i<ll:
      m[k]=l[i]
      i+=1
      k+=1
    while j<lr:
      m[k]=r[j]
      j+=1
      k+=1
    return nswaps
  return merge_sort(a)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    print(count_inversions(arr))

