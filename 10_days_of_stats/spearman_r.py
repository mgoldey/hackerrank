n=int(input())
x=[float(i) for i in input().strip().split()]
y=[float(i) for i in input().strip().split()]

def get_r(a):
  d={x:i for i,x in enumerate(sorted(a))}
  ra=[d[i] for i in a]
  return ra

rx=get_r(x)
ry=get_r(y)
r=0.0
for i,j in zip(rx,ry):
  r+=6*(i-j)**2
r/=n*(n**2-1)
r=1.0-r
print("{:.3f}".format(r))
