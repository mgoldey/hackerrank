# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
s=input().strip()
n=int(input().strip())
ls=len(s)
c=s.count("a")*math.floor(n//ls)+s[:n%ls].count("a")
print(c)
