n=int(input())
m=int(input())
regions=[]
data=[[int(i) for i in input().split()]for j in range(n)]
done=[]
todo=[]
for ix,i in enumerate(data):
  for jy,j in enumerate(i):
    if j==0:
      done.append([ix,jy])
    else:
      todo.append([ix,jy])
  


def get_neighbors(i,j):
  global todo,done
  c=[]
  for k in [-1+i,i,1+i]:
    for l in [-1+j,j,1+j]:
      loc=[k,l]
      if loc in todo:
        c+=[loc]
        todo.remove(loc)
        done.append(loc)
        c+=get_neighbors(k,l)
  return c    

cs=[]
while len(todo)>0:
  loc=todo.pop()
  done.append(loc)
  c=[loc]
  c+=get_neighbors(loc[0],loc[1])
  cs.append(c)
ls=[len(i) for i in cs]
print(max(ls))
