def bubbleSort(array):
  n=len(array)
  while True:
    swapped = False;
    for i in range(1,n,1):
     # print(i)
      if array[i-1]>array[i]:
        temp = array[i-1]
        array[i-1] = array[i]
        array[i] = temp
        swapped = True
    if swapped == False:
      break
  return [swapped, array]
