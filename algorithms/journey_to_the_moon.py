n,p=[int(i) for i in input().split()]
def fac(i):
  if i==0 or i==1:
    return 1
  return i*fac(i-1)
class astro():
  def __init__(self):
    self.neighbors=[self]
    self.visited=False
  def dfs(self,res):
    if self.visited==True:
      return 0
    res=1
    self.visited=True
    for ineighbor in self.neighbors:
      res+=ineighbor.dfs(res)
    return res
    
alist=[astro() for i in range(n)]

for l in range(p):
  a,b=[int(i) for i in input().split()]
  tmp=alist[a].neighbors
  alist[a].neighbors+=alist[b].neighbors
  alist[b].neighbors+=tmp
  
country_list=[]
singletons=0
for i in alist:
  if i.visited==False:
    res=i.dfs(0)
    if res>1:
      country_list.append(res)
    else:
      singletons+=1
    
n_countries=len(country_list)
nways=0
for i in range(n_countries):
  n1=country_list[i]
  for j in range(i+1,n_countries):
    n2=country_list[j]
    nways+=n1*n2
nways+=sum(country_list)*singletons
if singletons>1:
  nways+=int(singletons*(singletons-1)/2)
print(nways)       
