# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
a=[int(i) for i in input().split()]
from collections import defaultdict
d=defaultdict(lambda:0)
for i in a:
  d[i]+=1
m=sorted(d,reverse=True,key=lambda s:(d[s],1/s))
print(m[0])

