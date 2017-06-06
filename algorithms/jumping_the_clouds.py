# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input().strip())
c=[int(i) for i in input().split()]
jumps=0
i=0
while i<(n-1):
  if (i+2)<(n) and not c[i+2]:
    i+=2
    jumps+=1
  else:
    jumps+=1
    i+=1
  #print(i)
print(jumps)
