# Enter your code here. Read input from STDIN. Print output to STDOUT
c=0
l=[]
n=int(input())
for i in input().split():
  j=int(i)
  if j in l:
    l.remove(j)
    c+=1
  else:
    l.append(j)
print(c)
