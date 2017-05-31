n=5
x=[]
y=[]
for i in range(5):
  ix,iy=[int(i) for i in input().split()]
  x.append(ix)
  y.append(iy)

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
b=pearsonr(x,y)*stddev(y)/stddev(x)
a=mean(y)-b*mean(x)
print("{:.3f}".format(80*b+a))

