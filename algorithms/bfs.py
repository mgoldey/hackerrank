# Enter your code here. Read input from STDIN. Print output to STDOUT

edge_length=6

class node():
  def __init__(self):
    self.parent=None
    self.neighbors=[]
  def bfs(self):
    from collections import deque
    visited=[]
    queue=deque([self])
    while queue:
      cur=queue.popleft()
      visited.append(cur)
      for inode in cur.neighbors:
        if inode not in visited:
          queue.append(inode)
          inode.parent=cur
          visited.append(inode)
    return

q=int(input())

for iquery in range(q):
  num_nodes,num_edges=[int(i) for i in input().split()]
  nodes=[node() for i in range(num_nodes)]
  for edge in range(num_edges):
    start,end=[int(i)-1 for i in input().split()]
    if start==end:
     continue
    if nodes[end] in nodes[start].neighbors:
     continue
    if nodes[start] in nodes[end].neighbors:
     continue
    nodes[start].neighbors.append(nodes[end])
    nodes[end].neighbors.append(nodes[start])
    
  s=int(input())-1
  starting_node=nodes[s]
  starting_node.bfs()
  ds=[]
  for inode in nodes:
    if inode==starting_node:
      continue
    d=1
    cur=inode
    while cur.parent!=starting_node and cur.parent!=None:
      cur=cur.parent
      d+=1
    ds.append(d*edge_length if cur.parent==starting_node else -1)

  print(" ".join([str(i) for i in ds]))
