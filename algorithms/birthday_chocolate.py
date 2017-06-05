# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
s=[int(i) for i in input().strip().split()]
d,m=[int(i) for i in input().strip().split()]
c=0
for i in range(1+n-m):
  if sum(s[i:i+m])==d:
    c+=1
print(c)
