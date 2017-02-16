import numpy as np
import math
def pprint(ival):
  print("{:.1f}".format(ival))
n=int(input().strip())
a=np.array(input().strip().split(),dtype=int)
a.sort()
pprint(a.mean())
if n%2==1:
  lm=(n-1)//2
  pprint(a[lm])
else:
  lm=n//2-1
  pprint(.5*a[lm]+.5*a[lm+1])

c=np.unique(a,return_counts=True)
print(c[0][c[1]==c[1].max()].min())  
