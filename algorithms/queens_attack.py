# Enter your code here. Read input from STDIN. Print output to STDOUT
n,k=[int(i) for i in input().split()]
qx,qy=[int(i)-1 for i in input().split()]

def dist(x1,y1,x2,y2):  
  if x1==x2:
    return abs(y1-y2)
  if y1==y2:
    return abs(x1-x2)
  r=abs(x2-x1)+abs(y2-y1)
  r*=.5
  return(int(r))

b=n-1

# right, left, up, down, ru,lu,ld,rd
ref=[[n-1,qy],[0,qy],[qx,n-1],[qx,0]]# provides positions of maximum displacement
x,y=qx,qy
while x<b and y<b:
  x+=1
  y+=1
ref.append([x,y])
x,y=qx,qy
while y<b and x>0:
  x-=1
  y+=1
ref.append([x,y])
x,y=qx,qy
while x>0 and y>0:
  x-=1
  y-=1
ref.append([x,y])
x,y=qx,qy
while x<b and y>0:
  x+=1
  y-=1
ref.append([x,y])
#print(ref)
# get max moves
m=[dist(qx,qy,ix,iy) for ix,iy in ref]
#print(m)

for i_obst in range(k):
  xo,yo=[int(i)-1 for i in input().split()]
  d=dist(xo,yo,qx,qy)-1
  dx,dy=(xo-qx,yo-qy)
  if yo==qy:
    if xo>qx:
      m[0]=min(m[0],d)
    else:
      m[1]=min(m[1],d)
  elif xo==qx:
    if yo>qy:
      m[2]=min(m[2],d)
    else:
      m[3]=min(m[3],d)
  elif xo>qx and yo>qy:
    if dx!=dy:
      continue
    m[4]=min(m[4],d)
  elif xo<qx and yo>qy:
    if dx!=-dy:
      continue
    m[5]=min(m[5],d)
  elif xo<qx and yo<qy:
    if dx!=dy:
      continue
    m[6]=min(m[6],d)
  elif xo>qx and yo<qy:
    if dx!=-dy:
      continue
    m[7]=min(m[7],d)
  #print(xo,yo,m)
#print(m)  
print(sum(m))
