# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for itest in range(t):
  n=int(input())
  s=[sorted(input().strip()) for i in range(n)]
  f=True
  for i in range(n-1):
    t=sum([s[i][j]<=s[i+1][j] for j in range(n)])
    if t!=n:
      f=False
      break
  if f:
    print("YES")
  else:
    print("NO")
    
  
