from collections import defaultdict
import queue
class Graph():
  def __init__(self,data):
    self.nnodes=data
    self.edges=defaultdict(list)
  def connect(self,a,b):
    self.edges[a].append(b)
    self.edges[b].append(a)
  def find_all_distances(self,start):
    ds=[-1 for i in range(self.nnodes)]
    unvisited=[1 for i in range(self.nnodes)]
    q=queue.Queue()
    ds[start]=0
    unvisited[start]=0
    q.put(start)
    
    while not q.empty():
      n=q.get()
      children=self.edges[n]
      d=ds[n]
      for child in children:
        if unvisited[child]==1:
          q.put(child)
          unvisited[child]=0
          ds[child]=d+6
    
    ds.pop(start)
    print(" ".join([str(i) for i in ds]))
    
t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    s = int(input())
    graph.find_all_distances(s-1)
    

