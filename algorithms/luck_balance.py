# Enter your code here. Read input from STDIN. Print output to STDOUT
n,k=[int(i) for i in input().split()]

cs,imps=[[],[]]
l=0
for i in range(n):
  c,j=[int(k) for k in input().split()]
  if j==0:
    l+=c
    continue
  cs.append(c)
  imps.append(j)
cs=sorted(cs,reverse=True)
l+=sum(cs[:k])-sum(cs[k:])
print(l)
