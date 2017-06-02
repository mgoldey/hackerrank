queries=int(input().strip())
for iquery in range(queries):
  n,m=[int(i) for i in input().strip().split()]
  
grid=[[0 for i in range(m)] for j in range(n)]

def sum_grid(grid):
	s=0
	for i in grid:
		for j in i:
			s+=j
	return s

def isvalid(grid):
	n=len(grid)
	m=len(grid[0])
	for i in range(0,n-2,1):
		for j in range(0,m-2,1):
			if sum_grid(grid[i:i+3][j:j+3])<2:
				return [1,i,j]
			elif sum_grid(grid[i:i+3][j:j+3])>2:
				return [-1,i,j]
	return [0]

def get_ways(n,m):
	good=[]
	for i in range(n):
		for j in range(m):
			grid=[[0 for k in range(m)] for l in range(n)]
			grid[i][j]=1
			r=isvalid(grid)
			if r[0]==0:
				if grid not in good:
					good.append(grid)
				continue
			if r[0]==-1:
				continue
			if r[0]==1:
				
