res=[0,1,1,2,3,5]
while True:
  try: 
    n=int(input())
    while len(res)<(n+1):
      res.append(res[-1]+res[-2])
    print(res[n])
  except:
    break
