# Enter your code here. Read input from STDIN. Print output to STDOUT
n,k=[int(i) for i in input().split()]
a=[int(i ) for i in input().split()]
a=sorted(a)
c=0
for i in range(n):
  for j in range(i+1,n):
    if (a[i]+a[j])%k==0:
      c+=1
print(c)
