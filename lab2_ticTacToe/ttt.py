#Tac Toe Game -- DO NOT SUBMIT!
from tttlib import *

def endTurn():
  state = analyzeBoard(T)
  #print("State: (0 = in play, 1/2 = win, 3 = draw)" + str(analyzeBoard(T)))  #Prints state of game
  if state == -1:
    print("Error: invalid.argument <T> <player> tttlib.py")
    return False
  elif state == 1:
    printBoard(T)
    print("X Won")
    return False
  elif state == 2:
    printBoard(T)
    print("Y Won")
    return False
  elif state == 3:
    printBoard(T)
    print("Draw")
    return False
  else:
    return True


T = genBoard()
while True:
  printBoard(T)
  move = input("X move")
  if move == "0" or move == "1" or move == "2" or move == "3" or move == "4" or move == "5" or move == "6" or move == "7" or move == "8":
    move = int(move)
    if T[move] == 0:
      T[move] = 1
    else:
      #print("Error: position.occupied ttt.py")
      break
  else:
    #print("Error: invalid.input ttt.py")
    break
  end = endTurn()
  #print("End: " + str(end))
  if end == False:
    break
  if genWinningMove(T, 2) != -1:
    #print("Winner: (returns square position) " + str(genWinningMove(T, 2)))
    T[genWinningMove(T, 2)] = 2
  elif genNonLoser(T, 2) != -1:
    #print("Non Loser: (returns square position) " + str(genNonLoser(T, 2)))
    T[genNonLoser(T, 2)] = 2
  else:
    T[genOpenMove(T, 2)] = 2
    #T[genRandomMove(T, 2)] = 2
    #print("Random... see square: ")
  end = endTurn()
  if end == False:
    break
