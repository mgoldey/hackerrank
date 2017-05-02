max_w=9800
n=49
mean=205
std=15.
def gau(x,x0,s):
  import math
  pi=math.pi
  prefactor=1.0/(s*math.sqrt(2.*pi))
  exp=math.exp(-(x-x0)**2/(2.*s**2))
  return prefactor*exp


def f(x,x0,s):
  import math
  exp=(x-x0)/(s*math.sqrt(2.))
  return .5*(1.+math.erf(exp))

def pprint(i):
  print("{:0.4f}".format(i))


# For large n, the distribution of sample sums  is close to normal distribution with
# mean mu'=n*mu and stddev s'=s*(n**.5)

pprint(f(max_w,mean*n,std*n**.5))
