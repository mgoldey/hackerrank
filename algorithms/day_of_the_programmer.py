# Enter your code here. Read input from STDIN. Print output to STDOUT
d=dict()
for i,j in zip(range(9),[31,28,31,30,31,30,31,31,30]):
  d[i]=j
y=int(input())
ly=False
s=False
if y<1917:
  ly=y%4==0
if y>1919:
  ly=(y%4==0)*(y%100!=0)+(y%400==0)
if y==1918:
  s=True
  d[1]-=13
if ly:
  d[1]+=1

day=256
i=0
while (day-d[i])>0:
  day-=d[i]
  i+=1
print("{:}".format(day).zfill(2)+"."+"{:}".format(i+1).zfill(2)+"."+str(y))
  



