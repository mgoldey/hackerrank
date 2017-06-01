t = int(input().strip())
for a0 in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    for i in range(n):
      for j in range(i+1,n,1):
        if (a[i]+a[j])==m:
          print("{:} {:}".format(i+1,j+1))

