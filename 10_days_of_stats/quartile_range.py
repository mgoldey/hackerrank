import bisect
n=int(input().strip())
x=input().strip().split()
f=input().strip().split()

X=[]
F=[]
for i,j in zip(x,f):
  for k in range(int(j)):
    bisect.insort(X,int(i))

N=len(X)
  
def pprint(ival):
  print("{:.1f}".format(ival))
  

def median(b):
  lb=len(b)
  if lb%2==0:
    lm=lb//2-1
    return [.5*(b[lm]+b[lm+1]),lm+1]
  else:
    lm=(lb-1)//2
    return [b[lm],lm]
q2,lq2=median(X)
if N%2==1:
  q1,lq1=median(X[:lq2])
  q3,lq3=median(X[lq2+1:])
else:
  q1,lq1=median(X[:lq2])
  q3,lq3=median(X[lq2:])

pprint(q3-q1)
