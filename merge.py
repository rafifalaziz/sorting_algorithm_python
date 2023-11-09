# this sorting solved with approach of using stack instead of using recursion

def merge(arr):
  L = [{"array":arr, "status":False}]
  R = []
  choice = [L]
  while(len(L)>0):
    print()
    print("-----------------iteration----------------")
    print()
    
    if(L[-1]["status"] and R[-1]["status"]):
      i = j = k = 0
      print()
      print("when all true, Last choice ", choice[-1])
      print()
      while i < len(L[-1]["array"]) and j < len(R[-1]["array"]):
          if L[-1]["array"][i] <= R[-1]["array"][j]:
              choice[-1][-2]["array"][k] = L[-1]["array"][i]
              i += 1
          else:
              choice[-1][-2]["array"][k] = R[-1]["array"][j]
              j += 1
          k += 1

      while i < len(L[-1]["array"]):
          choice[-1][-2]["array"][k] = L[-1]["array"][i]
          i += 1
          k += 1

      while j < len(R[-1]["array"]):
          choice[-1][-2]["array"][k] = R[-1]["array"][j]
          j += 1
          k += 1
      L.pop()
      R.pop()
      choice[-1][-1]["status"] = True
      choice.pop()
      print()
      print("Pop choice ", choice[-1])
      print()
      print("after operation sort")
      print("Left Array ", L)
      print("Right Array ", R)
      print()
      if(L[0]["status"]):
        print()
        print("All Done")
        return L.pop()["array"]
    if(L[-1]["status"]):
      if(not R[-1]["status"]):
        choice.append(R)
        print()
        print("Append R to stack choice")
    if(not choice[-1][-1]["status"]):
      if(not L[-1]["status"] and not R):
        choice.append(L)
        print()
        print("Append L to stack choice")
      elif(not L[-1]["status"] and not R[-1]["status"]):
        choice.append(L)
        print()
        print("Append L to stack choice")
      last = choice[-1][-1]

      mid = len(last["array"])//2
      
      L.append({"array": last["array"][:mid], "status": True if len(last["array"][:mid])==1 else False})
      R.append({"array": last["array"][mid:], "status": True if len(last["array"][mid:])==1 else False})
      print()
      print("Dividing mid")
      print("L array ", L)
      print("R array ", R)

print(merge([
    54, 23, 76, 11, 89, 35, 42, 67, 28, 95,
    50, 19, 63, 81, 5, 72, 33, 47, 60, 14,
    92, 39, 88, 25, 70, 18, 78, 8, 99, 45,
    69, 30, 84, 3, 97, 55, 22, 71, 10, 65,
    85, 12, 83, 40, 91, 27, 74, 16, 94, 51,
    68, 37, 79, 7, 96, 57, 24, 73, 17, 86,
    62, 41, 87, 31, 98, 58, 21, 75, 13, 90,
    38, 66, 20, 77, 6, 82, 29, 93, 52, 64,
    80, 44, 61, 9, 100, 48, 59, 15, 37, 53,
    26, 36, 43, 1, 56, 32, 49, 4, 66, 69
]))