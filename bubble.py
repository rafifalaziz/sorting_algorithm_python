# this approach using nested looping

def bubble(arr):
  sortedIndex = len(arr)-1
  for i in range(len(arr)):
    for j in range(sortedIndex):
      if(arr[j]>arr[j+1]):
        arr[j], arr[j+1] = arr[j+1], arr[j]
    sortedIndex-=1
    print(arr)
  return arr