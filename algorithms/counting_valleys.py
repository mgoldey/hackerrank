n=int(input())
path=list(input().strip())
d={'U':1,'D':-1}
l=0
c=0
for i,step in enumerate(path):
  l+=d[step]
  #print(i,l)
  path[i]=l
  if i>0 and l<0 and path[i-1]>=0:
    c+=1
  elif i==0 and l<0:
    c+=1
print(c)    
  
