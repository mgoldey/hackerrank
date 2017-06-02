# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input().strip()) # NUM TEST CASES
for i in range(n):
  m=int(input().strip()) # NUM VALS
  a=[int(k) for k in input().strip().split()]
  found=False
  if m==1:
    found=True
    print("YES")
  elif m>2:
    s1=a[0]
    s2=sum(a[2:])
    if s1==s2:
        print("YES")
        found=True
    for j in range(2,m):
      s1+=a[j-1]
      s2-=a[j]
      if s1==s2:
        print("YES")
        found=True
        break
  if not found:
    print("NO")
  

    
