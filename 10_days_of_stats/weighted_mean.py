
def pprint(ival):
  print("{:.1f}".format(ival))
  
n=input().strip()
a=input().strip().split()
b=input().strip().split()
top=0.0
bottom=0.0
for i,j in zip(a,b):
  i=int(i)
  j=int(j)
  top+=i*j
  bottom+=j

pprint(top/bottom)
