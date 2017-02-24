import math
a=float(input().strip()) # DISCOVERED VALUE
b=float(input().strip()) # ACTUAL VALUE
e=math.e
def fac(i):
  if i>0:
    return math.gamma(i+1)
def pd(k,l): 
  """ Returns the probability of l given k"""
  x=l**k
  y=e**-l
  z=fac(k)
  return x*y/z

print("{:.3f}".format(pd(b,a)))
