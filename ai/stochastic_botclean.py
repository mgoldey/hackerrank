#!/bin/python3
def nextMove(posr, posc, board):
  for i in range(5):
    for j in range(5):
      if board[i][j]=='d':
        dx=i
        dy=j
        break
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
  
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    print(next(nextMove(pos[0], pos[1], board)))

