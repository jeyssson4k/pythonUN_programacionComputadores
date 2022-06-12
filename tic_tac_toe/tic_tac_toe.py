import math
import random

def assign(board,player,count):
  p = list(map(int,input().split(",")))
  count += 1
  board[p[0]-1][p[1]-1] = player
def pc_select():
  row = math.floor(random.random()*len(board))
  column = math.floor(random.random()*len(board))
  position = [row,column]
  return position
def pc_assign(board,position, count):
  row,column = position
  if(board[row][column] == 0):
    board[row][column] = 3
    count += 1
  else:
    while(board[row][column] != 0):
        position = pc_select()
        row,column = position
        if(board[row][column] == 0):
            board[row][column] = 3
            count += 1
            break

def verify(board,player):
  for i in range(len(board)):
    win = 0
    if board[i].count(player) == 3:
      return True
    elif not board[i].count(player) == 3:
      for j in range(len(board)):
        if board[j][i] == player:
          win += 1
          if(win == 3):
            return True
    else:
      return False
def refresh(board):
  for i in board:
    for j in i:
      if(j == 0):
        print("*",end=" ")
      elif(j == 1):
        print("x",end=" ")
      elif(j == 2 or j == 3):
        print("o",end=" ")
    print()


board = [
  [0,0,0],
  [0,0,0],
  [0,0,0]
]
win = False
count = 0
while(count < 9 or win == False):
  assign(board,1,count)
  if(verify(board,1) == True):
    print(True)
    break
  if(count == 9):
    print(False)
    break
  pos = pc_select()
  pc_assign(board,pos,count)
  if(verify(board,3) == True):
    print(False)
    break
  refresh(board)
