def selection(arr):
  min = 9999999
  indexMin = None
  indexArr = 0
  i = 0
  while(indexArr < len(arr)-1):
    if(arr[i]<min):
      min = arr[i]
      indexMin = i
    if(i == len(arr)-1):
      temp = arr[indexArr]
      arr[indexArr] = arr[indexMin]
      arr[indexMin] = temp
      min = 9999999
      indexArr+=1
      i=indexArr
    i+=1
  return arr