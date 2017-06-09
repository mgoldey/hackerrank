# Enter your code here. Read input from STDIN. Print output to STDOUT
n,k=[int(i) for i in input().split()]
h=sorted([int(i) for i in input().split()])
i=0
c=0
while i<n:
  c+=1
  l=h[i]+k
  while i<n and h[i]<=l:
    i+=1
  l=h[i-1]+k
  while i<n and h[i]<=l:
    i+=1
print(c)
