# Enter your code here. Read input from STDIN. Print output to STDOUT
d=[0 for i in range(100)]
n=int(input())
for i in input().split():
  d[int(i)]+=1
print(" ".join([str(i) for i in d]))
