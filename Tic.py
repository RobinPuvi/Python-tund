#Copyright Kristjan Nõmm 2022
#For personal use only
import os
import sys

#TODO COLOUR 
#os.system("color")

#usernames
name_player1= input("Player 1, Enter your name-> ")
name_player2= input("Player 2, Enter your name-> ")
if name_player2 == "debug":
    print (name_player1)
    print (name_player2)
#clear before game
if name_player2 == "debug":
    print ("Debug mode")
else:
    #Windows (NT)
    os.system("cls" if os.name == "nt"
    #Linux/Unix
    else "clear")
# board and empty places
board=["0","1","2","3","4","5","6","7","8"]
empty = [0,1,2,3,4,5,6,7,8]
# def function
def display_board():
    #   |   |   
    # 0 | 1 | 2
    #   |   |   
    # ---------
    #   |   |   
    # 3 | 4 | 5
    #   |   |   
    # ---------
    #   |   |   
    # 6 | 7 | 8
    #   |   |   
    board_brake = ("  |   |   ")
    board_space = ("---------")
    print(board_brake)
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board_brake)
    print(board_space)
    print(board_brake)
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board_brake)
    print(board_space)
    print(board_brake)
    print(board[6]+" | "+board[7]+" | "+board[8])
    print(board_brake)

print (display_board())

def player_input(player):
    player_symbol = ["X","O"]
    correct_input = True
    if correct_input == False:
        print = "Vale sisend"
    position = int(input("Player {playerNo} chance! Choose field to fill {symbol} -> ".format(playerNo = player +1, symbol = player_symbol[player])))
    if board[position] == "X" or board[position] == "O":
        correct_input = False
    if not correct_input:
        print("Position already equipped")
        player_input(player)
    else:
        empty.remove(position)
        board[position] = player_symbol[player]
        return 1
#function checks if any player won

def check_win():
  #define players symbols and winning positions
  player_symbol = ["X","O"]
  winning_positions =[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

  #check all winning positions for matching placements
  for check in winning_positions:
    first_symbol = board[check[0]]
    if first_symbol != " ":
      won = True
      for point in check:
        if board[point] !=  first_symbol:
          won = False
          break
      if won:
        if first_symbol == player_symbol[0]:
          print("player 1 won")
        else:
          print("player 2 won")
        break
    else:
      won = False
  if won:
    return 0
  else:
    return 1

#function to invoke functions to play

def play():
  player = 0
  while empty and check_win():    
    display_board()
    player_input(player)
    player = int(not player)
  if not empty:
    print("NO WINNER!")

#driver code
if __name__ == "__main__":
  play()

sys.exit()