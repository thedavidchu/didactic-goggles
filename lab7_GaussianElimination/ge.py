#START HELPER FUNCTIONS
def error(matrix):
  try:
    if type(matrix) != list:
      return False
    elif len(matrix) == 0:
      return False
    elif len(matrix[0]) == 0:
      return False
    for i in range(0,len(matrix),1):
      if len(matrix[i]) != len(matrix[0]):
        return False
  except:
    return False

#END HELPER FUNCTIONS


def ge_fw(matrix):
  if error(matrix) == False:
    print("Error in Matrix")
    return -1

  mOut=list(matrix)

  if len(mOut) > len(mOut[0]):
    r = len(mOut[0])
  else:
    r = len(mOut)

  for d in range(0,r,1): #Diagonal
    for y in range(d,len(mOut[0]),1): #Column
      for x in range(d,len(mOut),1): #Row
        if mOut[x][y] != 0: #Bring non-zero to d-th row
          temp = list(mOut[d])
          mOut[d] = list(mOut[x])
          mOut[x] = list(temp)
          break
      for i in range(d+1,len(mOut),1):
        if mOut[i][y] != 0:
          mult = mOut[i][y]/mOut[d][y]
          for j in range(0,len(mOut[0]),1): #Row Reduce
            mOut[i][j] = mOut[i][j] - mult*mOut[d][j]
          mult = mOut[d][y]
          for j in range(0,len(mOut[0]),1): #Divide by leading value
            mOut[d][j] = mOut[d][j]/mult
      d=y

  return mOut


def ge_bw(matrix):
  #ERROR
  if error(matrix) == False:
    print("Error in Matrix")
    return -1

  mOut=list(ge_fw(matrix))

  #swap to find an empty column
  if len(mOut) > len(mOut[0]):
    r = len(mOut[0])
  else:
    r = len(mOut)

  for y in range(len(mOut[0])-1,-1,-1):
    for x in range(len(mOut)-1,-1,-1):
      if mOut[x][y] != 0:
        #Row reduce above
        for i in range(0,x,1):
          mult = mOut[i][y]/mOut[x][y]
          for j in range(0,len(mOut[0]),1):
            mOut[i][j] = mOut[i][j] - mult*mOut[x][j]

  return mOut

def main():
  print( ge_bw([ [0,1,73],[0,0,23],[0,23,42],[0,23,6] ]) )
 # print( ge_bw([ [9,1,73,12],[4,0,23,21],[34,23,42,43] ]) )
main()
