p = int(input().strip())
def isprime(a):
  import math
  if a<2:
    return("Not prime")

  for i in range(2,1+math.floor(math.sqrt(a)),1):
    if a%i==0:
      return("Not prime")
  return("Prime")

for a0 in range(p):
    n = int(input().strip())
    print(isprime(n))


