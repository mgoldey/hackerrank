import bisect
n=input().strip()
a=input().strip().split()
li=[]
for i in a:
  bisect.insort(li,int(i))

def median(b):
  lb=len(b)
  if lb%2==0:
    lm=lb//2-1
    return [int(.5*(b[lm]+b[lm+1])),lm+1]
  else:
    lm=(lb-1)//2
    return [b[lm],lm]
q2,lq2=median(li)
if len(li)%2==1:
  q1,lq1=median(li[:lq2])
  q3,lq3=median(li[lq2+1:])
else:
  q1,lq1=median(li[:lq2])
  q3,lq3=median(li[lq2:])
print(q1)
print(q2)
print(q3)

