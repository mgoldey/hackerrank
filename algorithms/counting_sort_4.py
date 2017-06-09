# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
d=defaultdict(lambda:[0,[]])
n=int(input())
for i in range(n):
  j,k=input().split()
  j=int(j)
  if i<(n/2):
    k="-"    
  d[j][0]+=1
  d[j][1].append(k)
ret_str=""
for i in range(100):
  ret_str+=" ".join(d[i][1])+" "
print(ret_str)
  
  
    
  
  
