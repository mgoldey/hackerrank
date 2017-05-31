import numpy as np
m,n=[int(i) for i in input().split()]
x=[]
y=[]
for i in range(n):
  inp=[float(i) for i in input().split()]
  x.append(inp[:m])
  y.append(inp[-1])

#center
x=np.array(x)
y=np.array(y)
x_r = x-np.mean(x,axis=0)
y_r = y-np.mean(y)

beta = np.linalg.inv(x_r.T@x_r)@(x_r.T@y_r)

nnew=int(input())
for i in range(nnew):
  inp=np.array([float(i) for i in input().split()])
  x_new=inp-np.mean(x,axis=0)
  r=x_new@beta+np.mean(y)
  print("{:.2f}".format(np.round(r,2)))
  
