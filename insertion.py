class Node:
  def __init__(self, val):
    self.next = None
    self.val = val

class LinkedList:
  def __init__(self):
    self.head = None

  def firstHead(self, val):
    newNode = Node(val)
    newNode.next = self.head
    self.head = newNode

  def insertLast(self, val):
    newNode = Node(val)
    buffer = self.head
    while(buffer.next!=None):
      buffer = buffer.next
    buffer.next = newNode

  def insertNext(self, previous, val):
    newNode = Node(val)
    newNode.next = previous.next
    previous.next = newNode

  def prevBiggerNode(self, val):
    if(self.head.val < val):
      return 'first'
    buffer = self.head
    bufferPrev = None
    while(buffer.val > val):
      bufferPrev = buffer
      buffer = buffer.next
      if(buffer == None):
        break
    if(buffer == None):
      return 'last'
    else:
      return bufferPrev

def insertion(arr):
  val = arr[0]
  node = Node(val)
  firstNode = LinkedList()
  firstNode.head = node
  for i in range(1, len(arr)):
    if(firstNode.prevBiggerNode(arr[i]) == 'first'):
      firstNode.firstHead(arr[i])
    elif(firstNode.prevBiggerNode(arr[i]) == 'last'):
      firstNode.insertLast(arr[i])
    else:
      firstNode.insertNext(firstNode.prevBiggerNode(arr[i]), arr[i])
  newArr = []
  buffer = firstNode.head
  while(buffer != None):
    newArr.append(buffer.val)
    buffer = buffer.next
  return newArr

print(insertion([92, 45, 17, 68, 31, 53, 77, 22, 84, 10, 60, 5, 49, 73, 38, 88, 19, 64, 25, 97, 14, 70, 33, 55, 81, 42, 76, 29, 90, 12, 61, 7, 93, 50, 80, 36, 72, 15, 67, 24, 98, 39, 87, 3, 56, 71, 21, 66, 9, 95, 35, 74, 18, 89, 2, 58, 85, 27, 99, 1, 46, 79, 40, 78, 16, 63, 6, 94, 32, 82, 44, 65, 11, 91, 51, 75, 37, 86, 4, 57, 69, 20, 96, 8, 62, 23, 83, 30, 47, 83, 28, 54, 41, 100, 59, 26, 48, 52, 34]))
