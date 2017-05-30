def getBiggestRegion(grid):
  import math
  regions=0
  locs=[]
  n=len(grid)
  m=len(grid[0])
  for i in range(n):
    for j in range(m):
      if grid[i][j]==1:
        regions+=1
        locs.append([[i,j]])
  def isneighbor(l1,l2):
    i1,j1=l1
    i2,j2=l2
    if abs(i1-i2)==1 and j1==j2:
      return True
    if abs(j1-j2)==1 and i1==i2:
      return True
    if abs(j1-j2)==1 and abs(i1-i2)==1:
      return True
    return False

  for r1 in range(regions):
    for r2 in range(r1+1,regions):
      neighbor=False
      for l1 in locs[r1]:
        for l2 in locs[r2]:
         if isneighbor(l1,l2):
          neighbor=True
      if neighbor:
        for l in locs[r2]:
          if l not in locs[r1]:
            locs[r1]+=[l]
        locs[r2]=locs[r1]
  rmax=0
  for r in range(regions):
    rmax=rmax if rmax>len(locs[r]) else len(locs[r])
  return rmax

n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
print(getBiggestRegion(grid))

