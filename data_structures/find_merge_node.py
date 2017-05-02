"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def FindMergeNode(headA, headB):
  ns1=[]
  ns2=[]
  n1=headA
  n2=headB
  while n1!=None:
    ns1.append(n1)
    n1=n1.next
  while n2!=None:
    ns2.append(n2)
    n2=n2.next
  for i in ns1:
    if i in ns2:
      return i.data
  for j in ns2:
    if j in ns1:
      return j.data
  return None
