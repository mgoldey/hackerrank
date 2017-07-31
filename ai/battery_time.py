#!/bin/python3

import sys
import numpy as np
timeCharged = float(input().strip())
data=open("trainingdata.txt").read().splitlines()
percs=[]
times=[]
for i in data:
  i=i.split(',')
  percs.append(float(i[0]))
  times.append(float(i[1]))
full=np.array(sorted(zip(percs,times),key=lambda l:l[0]))
percs=np.array(full[:,0])
times=np.array(full[:,1])
percs=percs[times<8.00]
percs=percs.reshape(len(percs),1)
times=times[times<8.00]
x=percs
y=times
beta=np.linalg.inv(x.T@x)@(x.T@y)
if timeCharged>percs[-1]:
  print("8.00")
else:
  print("{:.2f}".format(beta[0]*timeCharged))
