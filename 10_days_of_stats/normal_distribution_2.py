import math

a,b=input().strip().split()
a=float(a)
b=float(b)
thr1=float(input().strip())
thr2=float(input().strip())

def pprint(i):
  print("{:.2f}".format(i*100))

def gau(x,x0,s):
  pi=math.pi
  prefactor=1.0/(s*math.sqrt(2.*pi))
  exp=math.exp(-(x-x0)**2/(2.*s**2))
  return prefactor*exp

def f(x,x0,s):
  exp=(x-x0)/(s*math.sqrt(2.))
  return .5*(1.+math.erf(exp))

pprint(1.0-f(80.,a,b))
pprint(1.0-f(60.,a,b))
pprint(f(60.,a,b))
