
a,b=input().strip().split()
a=float(a)
b=float(b)
from math import e
from math import gamma

def fac(i):
  if i>0:
    return gamma(i+1)
  if i==0:
    return 1
def pd(k,l):
  """ Returns the probability of k given mean of l """
  x=l**k
  y=e**-l
  z=fac(k)
  return x*y/z

def pprint(i):
  print("{:.3f}".format(i))
  
costa=0.0
costb=0.0
for i in range(50):
  i=float(i)
  costa+=pd(i,a)*(160+40*i**2)
  costb+=pd(i,b)*(128+40*i**2)
pprint(costa)
pprint(costb)
