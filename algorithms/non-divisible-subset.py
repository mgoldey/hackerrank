# Enter your code here. Read input from STDIN. Print output to STDOUT
n,k=[int(i) for i in input().split()]
a=[int(i)%k for i in input().split()] # ALREADY DO MODULO ARITHMATIC
from collections import defaultdict
d=defaultdict(lambda:0)
for i in a:
  d[i]+=1
c=0
for ikey in d.keys():
  if ikey==0:
    c+=1
    d[ikey]=0
    continue
  jkey=k-ikey
  if jkey in d.keys() and jkey!=ikey:
    c+=max(d[ikey],d[jkey])
    d[jkey]=0
  elif ikey!=k/2:
    c+=d[ikey]
  elif ikey==jkey: # ikey
    c+=1
  else:
    print("ERROR")
  d[ikey]=0
print(c)
