# Enter your code here. Read input from STDIN. Print output to STDOUT
n,q=[int(i) for i in input().split()]
seqList=[[] for i in range(n)]
lastAnswer=0
for iq in range(q):
  tq,x,y=[int(i) for i in input().split()]
  if tq==1:
    ix=(x^lastAnswer)%n
    seqList[ix].append(y)
  else:
    ix=(x^lastAnswer)%n
    lx=len(seqList[ix])
    lastAnswer=seqList[ix][y%lx]
    print(lastAnswer)

