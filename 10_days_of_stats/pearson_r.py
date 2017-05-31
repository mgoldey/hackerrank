n=int(input())
x=[float(i) for i in input().strip().split()]
y=[float(i) for i in input().strip().split()]

def mean(l):
  m=0.
  for i in l:
    m+=i
  m/=len(l)
  return(m)

def stddev(l):
  import math
  s=0.0
  m=mean(l)
  for i in l:
    s+=(i-m)**2
  s=math.sqrt(s/len(l))
  return s

def pearsonr(a,b):
  ma=mean(a)
  mb=mean(b)
  sa=stddev(a)
  sb=stddev(b)
  r=0.0
  for i,j in zip(a,b):
    r+=(i-ma)*(j-mb)
  r/=len(a)*sa*sb
  return r

print("{:.3f}".format(pearsonr(x,y)))
  
