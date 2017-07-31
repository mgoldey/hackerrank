def next_move(posx, posy, dimx, dimy, board):
  def pprint(b):
    for i in b:
        print(i)
  def count_dirty(board):
    c=0
    for i in board:
      for j in i:
        if j=="d":
          c+=1
    return c
  def dist(x1,y1,x2,y2):
    return(abs(x1-x2)+abs(y1-y2))
  def get_dirty(board):
    l=[]
    for i in range(len(board)):
      for j in range(len(board[0])):
        if board[i][j]=="d":
          l.append([i,j])
    return l
  def get_next(r,c,b):
    ls=get_dirty(b)
    ds=[dist(r,c,d[0],d[1]) for d in ls]
    n=sorted(zip(ds,ls))
    for i in n:
      yield i[1]

  while count_dirty(board)!=0:
    #pprint(board)
    dx,dy=next(get_next(posx,posy,board))
    while posx!=dx or posy!=dy:
      if posx>dx:
        posx-=1
        yield("UP")
      elif posx<dx:
        posx+=1
        yield("DOWN")
      if posy>dy:
        posy-=1
        yield("LEFT")
      elif posy<dy:
        posy+=1
        yield("RIGHT")
    yield("CLEAN")
    board[posx][posy]='-'

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    print(next(next_move(pos[0], pos[1], dim[0], dim[1], board)))

