# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for test_case in range(n):
  a,b=[int(i) for i in input().split()]
  ia,ib=int(a**.5),int(b**.5)
  z=[]
  for i in range(ia,ib+1,1):
    i2=i*i
    if i2>=a and i2<=b:
      z.append(i2)
  print(len(z))

