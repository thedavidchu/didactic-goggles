#Tic Tac Toe

def genBoard():
  return [0, 0, 0, 0, 0, 0, 0, 0, 0]

def printBoard(T):
  B = []
  #Errors, Making 1=>X and 2=>O:
  if len(T) == 9 and type(T) == list:
    i = 0
    for j in T:
      if j == 0:
        B = B[0:i] + [i]
      elif j == 1:
        B = B[0:i] + ["X"]
      elif j == 2:
        B = B[0:i] + ["O"]
      else:
        return False
      i = i + 1
  else:
    return False
  #Print Board:
  print(" " + str(B[0]) + " | " + str(B[1]) + " | " + str(B[2]))
  print("---|---|---")
  print(" " + str(B[3]) + " | " + str(B[4]) + " | " + str(B[5]))
  print("---|---|---")
  print(" " + str(B[6]) + " | " + str(B[7]) + " | " + str(B[8]))
  return True

def analyzeBoard(T):
  #Errors(length == 9, type == list, twos < ones, ones < twos + 1)
  if len(T) != 9 or type(T) != list:
    return -1
  else:
    zeros = 0
    ones = 0
    twos = 0
    for h in T:  #Count 0s, 1s, and 2s
      if h == 0:
        zeros = zeros + 1
      elif h == 1:
        ones = ones + 1
      elif h == 2:
        twos = twos + 1
      else:  #Ensure all values are == 0, 1, or 2
        return -1
#    if twos > ones: #Ensure PlayerX didn't miss a turn
#      return -1
#    elif ones > twos + 1: #Ensure PlayerO didn't miss a turn
#      return -1                           #THESE PREVENTED NON LOSING FROM WORKING
  #Winning:
  for k in range(1, 3, 1):
    if T[0] == k and T[1] == k and T [2] == k:
      return k
    elif T[3] == k and T[4] == k and T [5] == k:
      return k
    elif T[6] == k and T[7] == k and T [8] == k:
      return k
    elif T[0] == k and T[3] == k and T [6] == k:
      return k
    elif T[1] == k and T[4] == k and T [7] == k:
      return k
    elif T[2] == k and T[5] == k and T [8] == k:
      return k
    elif T[0] == k and T[4] == k and T [8] == k:
      return k
    elif T[2] == k and T[4] == k and T [6] == k:
      return k
  #Draw and In Play:
  if zeros == 0:
    return 3
  else:
    return 0

def error(T, player):
  if len(T) != 9 or type(T) != list or (player != 1 and player != 2):
    return False
  zeros = 0
  ones = 0
  twos = 0
  for h in T:
    if h == 0:
      zeros += 1
    elif h == 1:
      ones += 1
    elif h == 2:
      twos += 1
    else:
      return False
  if twos > ones:
    return False
  elif ones > twos + 1:
    return False
  elif zeros == 0:
    return False
  else:
    return True

def genNonLoser(T, player):
  if error(T, player) == False:
    return -1
  #Check board for open space that will result in win
  for i in range(0, 9, 1):
    newT = list(T)  #Resets every time
    if T[i] == 0 and player == 1:
      newT[i] = 2
    elif T[i] == 0 and player == 2:
      newT[i] = 1
    #Moves if prevents loss. Note: (a) it cannot cause a win; the opposite pieceis inserted, (b) it cannot cause a draw; function is not told to look for draw
    if (player == 2 and analyzeBoard(newT) == 1) or (player == 1 and analyzeBoard(newT) == 2):
      return i
  return -1

def genWinningMove(T, player):
  #Errors:
  if error(T, player) == False:
    return -1
  #Check board for open space that will result in win
  for i in range(0, 9, 1):
    newT = list(T)
    if T[i] == 0:
      newT[i] = player
      #Check for Win
      if analyzeBoard(newT) == player:
        return i
  return -1

def genRandomMove(T, player):
  #Errors:
  if error(T, player) == False:
    return -1
  #Generate random move
  while True:
    import random
    rand = random.randint(0, 8)
    if T[rand] == 0:
      return rand

def genOpenMove(T, player):
  #Errors:
  if error(T, player) == False:
    return -1
  #Check board for open space
  for i in range(0, 9, 1):
    if T[i] == 0:
      return i
