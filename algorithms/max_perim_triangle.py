n=int(input())
s=sorted([int(i) for i in input().split()])
while len(s)>=3:
  trial=s[-3:]
  if sum(trial[:2])<=trial[-1]:
    s.pop()
  else:
    break
if len(s)>=3:
  t=s[-3:]
  print(" ".join([str(i) for i in t]))
else:
  print(-1)
    
