def display_board(board):
  print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
  print("------------")
  print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
  print("------------")
  print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")

def player_move(board, choice, player_name):
  symbol = 'X' if player_name == 'Player 1' else 'O'
  count = 0
  for i in range(len(board)):
    for j in range(len(board[i])):
      count+=1
      if count == choice:
        if board[i][j] == " ":
          board[i][j] = symbol
          display_board(board)
          return True
        else:
          return False

def check_win(moves):
  win_condition = [
    [1,2,3],[4,5,6],[7,8,9],
    [1,4,7],[2,5,8],[3,6,9],
    [1,5,9],[3,5,7]
  ]
  win = False
  for i in win_condition:
    condition = []
    for move in sorted(moves):
      if move in i:
        condition.append(move)
    print(condition)
    if condition in win_condition:
      win = True
      break

  return win
def tic_tac_toe(p1, p2):
  board = [[" "," "," "],[" "," "," "],[" "," "," "]]
  p1_choices = []
  p2_choices = []
  while True:
    if p1+p2 == 9:
      print('TIE!')
      break
    if p1 <= p2:
      choice = input("Player 1 please enter a value from 1-9: ")
      if choice.isnumeric() == False:
        print ('Please choose a NUMBER from 1-9')
        continue
      choice = int(choice)
      if choice < 1 or choice > 9:
        print('Please choose value within 1-9')
        continue 
      if not player_move(board, choice, 'Player 1'):
        print('Spot already taken')
        continue 
      p1_choices.append(choice)
      if check_win(p1_choices):
        print('Player 1 wins!')
        break
      p1+=1
    else:
      choice = input("Player 2 please enter a value from 1-9: ")
      if choice.isnumeric() == False:
        print ('Please choose a NUMBER from 1-9')
        continue
      choice = int(choice)
      if choice < 1 or choice > 9:
        print('Please choose value within 1-9')
        continue 
      if not player_move(board, choice, 'Player 2'):
        print('Spot already taken')
        continue 
      p2_choices.append(choice)
      if check_win(p2_choices):
        print('Player 2 wins!')
        break
      p2+=1

tic_tac_toe(0,0)