n=int(input().strip())
a=input().strip().split()
li=[]
for i in a:
  li.append(int(i))
  
def pprint(ival):
  print("{:.1f}".format(ival))
  
m=0  
for i in li:
  m+=i
m/=n
s=0
for i in li:
  s+=((i-m)**2)
s/=n
s=s**.5
pprint(s)
