#!/usr/bin/python

# Head ends here
def next_move(posr, posc, board):
  def count_dirty(board):
    c=0
    for i in board:
      for j in i:
        if j=="d":
          c+=1
    return c
  def get_next(r,c,b):
    scope=[i for i in range(5)]
    for n in range(1,5):
      for i in range(r-n,r+n+1):
        for j in range(c-n,c+n+1):
          if i in scope and j in scope:
            if b[i][j]=='d':
              return [i,j]
    return -1
    
  while count_dirty(board)!=0:
    dx,dy=get_next(posr,posc,board)
    while posr!=dx or posc!=dy:
      if posr>dx:
        posr-=1
        yield("UP")
      elif posr<dx:
        posr+=1
        yield("DOWN")
      if posc>dy:
        posc-=1
        yield("LEFT")
      elif posc<dy:
        posc+=1
        yield("RIGHT")        
    yield("CLEAN")
    board[posr][posc]='-'
  return ""  

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    print(next(next_move(pos[0], pos[1], board)))

