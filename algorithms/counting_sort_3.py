# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
d=[0 for i in range(100)]
for i in range(n):
  j,k=input().split()
  d[int(j)]+=1
s=0
ret_str=""
for i in range(100):
  s+=d[i]
  ret_str+=str(s)+" "
print(ret_str)
