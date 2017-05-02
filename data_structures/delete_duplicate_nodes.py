"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def RemoveDuplicates(head):
  if head==None:
    return head
  n=RemoveDuplicates(head.next)
  if n==None:
    return head
  if head.data==n.data:
    head.next=n.next
    return head
  return head
  
  
  
  
  
  
  
  
  
  

