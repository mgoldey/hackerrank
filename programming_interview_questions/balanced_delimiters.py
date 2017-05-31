inp=input()
o=['{','[','(']
c=['}',']',')']
m={}
for i,j in zip(c,o):
  m[i]=j
running=""
for i in inp:
  if i in o:
    running+=i
    continue
  if running[-1]==m[i]:
    running=running[:-1]
  else:
    break
if len(running)==0:
  print("True")
else:
  print("False")


