#FUNCTIONS ASSIGNMENT

#CONTAINS
def contains(aList, item):
  for el in aList:
    if el == item:
      return True
  return False

#INDEXOF 
def indexOf(aList, item):
  for i, val in enumerate(aList):
    if val == item:
      return i
  return -1

test = [1, 2, 3, 4, 5, 6]
index = indexOf(test, 8)
if index != -1:
  print(f"8 IN list at {index}")
else:
  print("8 NOT in list")

    
#REVERSE
def reverse(aList):
    reversedList = []
    for i in range(len(aList)-1, -1, -1):
        reversedList.append(aList[i])
    return reversedList

test = [2, 4, 6, 8, 10]
reversed = reverse(test)
print(reversed)

#SWAP
#def swap(aList, idx1, idx2):
#  aList[idx1], aList[idx2] = aList[idx2], aList[idx1]
#  return aList

#aList = [1, 2, 3, 4, 5]
#idx1, idx2 = 1,2

#print(swap(aList, idx2, idx1))


#INDEXOFMIN
def indexOfMin(aList):
    minIndex = 0
    #ADD A COUNTER
    for i, element in enumerate(aList):
        if element < aList[minIndex]:
            minIndex = i
    return minIndex
  
test = [2, 4, 6, 8, 10]
minIndex = indexOfMin(test)
print(minIndex)


