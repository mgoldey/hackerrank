
def has_cycle(head):
  li=[]
  node=head
  while True:
    if node==None:
      return False
    if head in li:
      return True
    li.append(head)
    node=node.next
