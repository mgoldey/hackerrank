#!/bin/python3

solved={}
def make_change(coins, n):
    lc=len(coins)
    if coins==[] or n<0:
      return 0
    elif n==0:
      return 1
    elif not (lc,n) in solved:
      res=0
      for icoin,coin in enumerate(coins):
        if (n-coin)>=0:
          res+=make_change(coins[icoin:],n-coin)
      solved[(lc,n)]=res
      #print(coins,n,res)
    return solved[(lc,n)]

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
coins=sorted(coins,reverse=True)
#print(coins)
print(make_change(coins, n))

