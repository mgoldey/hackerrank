# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
a=sorted([int(i) for i in input().split()])
md=a[-1]-a[0]
if len(a)==1:
  print(-1)
elif len(a)==2:
  print(" ".join([str(i) for i in (a[0],a[1])]))
else:
  l=[]
  la=len(a)
  for i in range(la-1):
    j=i+1
    d=abs(a[j]-a[i])
    if d<md:
      l=[(a[i],a[j])]
      md=d
    elif d==md:
      l.append((a[i],a[j]))
  ret_str=""
  for ipair in l:
    ret_str+=" ".join([str(i) for i in ipair])+" "
  print(ret_str)
