n,k=[i for i in input().split()]
k=int(k)
r={}
r[n]=str(sum([int(i) for i in n]))
def get_rds(d):
  global r
  if len(d)==1:
    return d
  for i in r.keys():
    if i in d:
      d=d.replace(i,r[i])
  m=d[:2]
  r[m]=str(sum([int(i) for i in m]))
  d=d.replace(m,r[m])
  return get_rds(d)
print(get_rds(r[n]*k))
  
