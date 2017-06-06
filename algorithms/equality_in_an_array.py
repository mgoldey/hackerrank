# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
a=[int(i) for i in input().split()]
from collections import defaultdict
d=defaultdict(lambda:0)
for i in a:
  d[i]+=1
c=0
while max(d.values())!=sum(d.values()):
  l=sorted(zip(list(d.values()),list(d.keys())))
  lm=min(l)[1]
  c+=d.pop(lm)
print(c)

  

