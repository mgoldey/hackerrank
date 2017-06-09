# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
from math import log,floor
counter=3
while t>counter:
  t=t-counter
  counter*=2
print(counter-t+1)
