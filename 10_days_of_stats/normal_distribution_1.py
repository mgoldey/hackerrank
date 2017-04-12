import math

a,b=input().strip().split()
a=float(a)
b=float(b)
thr1=float(input().strip())
t0,t1=input().strip().split()
t0=float(t0)
t1=float(t1)

def pprint(i):
  print("{:3f}".format(i))
  
def gau(x,x0,s):
  pi=math.pi
  prefactor=1.0/(s*math.sqrt(2.*pi))
  exp=math.exp(-(x-x0)**2/(2.*s**2))
  return prefactor*exp

p1=0.0
xmax=5000
for i in range(xmax):
  p1+=gau(thr1*(i+1.)/xmax,a,b)
p1*=thr1*1./xmax
pprint(p1)

p2=0.0
xmax=5001
for i in range(xmax):
  p2+=gau(t0+(i/xmax)*(t1-t0),a,b)
p2*=(t1-t0)/xmax
pprint(p2)


