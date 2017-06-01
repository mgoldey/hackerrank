# Dynamic programming solution with permutations achieved via indexing change
s = int(input().strip())
def fac(i):
  if i==1 or i==0:
    return 1
  else:
    return i*fac(i-1)
def permut(k,l):
  return fac(k)/fac(k-l)
for a0 in range(s):
    n = int(input().strip())
    steps=[1,2,3]
    ls=len(steps)
    res=[[0 for j in range(ls+1) ] for i in range(0,n+1,1)]
    res[0][0]=1 # ONLY 1 WAY TO COUNT TO 0 WITH NO STEPS
    for j in range(1,ls+1,1):
      res[0][j]=1 # ONLY 1 WAY TO COUNT TO 0 WITH ANY STEPS
    for i in range(0,n+1,1):
      for j in range(1,ls+1,1):
        s=steps[j-1]
        if (i-s)>=0:
          res[i][j]=res[i-s][ls]+res[i][j-1] # instead of [i-s][j], we use [i-s][ls] since order matters
        else:
          res[i][j]=res[i][j-1]
    print(res[-1][-1])

