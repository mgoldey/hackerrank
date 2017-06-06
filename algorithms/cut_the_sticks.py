# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
s=[int(i) for i in input().split()]
while sum(s)>0:
  sm=min(s)
  c=0
  for i in range(len(s)):
    if s[i]>0:
      s[i]-=sm
      c+=1
  for i in range(s.count(0)):
    s.remove(0)
  print(c)
  
