#FUNCTIONS ASSIGNMENT

#CONTAINS
def contains(aList, item):
  for el in aList:
    if el == item:
      return True
  return False

#INDEXOF 
def indexOf(aList, item):
  #ADD A COUNTER
    for i, element in enumerate(aList):
        if element == item:
            return i
    return -1

#REVERSE
def reverse(aList):
    reversedList = []
    for i in range(len(aList)-1, -1, -1):
        reversedList.append(aList[i])
    return reversedList

#SWAP
#def swap(aList, idx1, idx2):
#  aList[idx1], aList[idx2] = aList[idx2], aList[idx1]
#  return aList

#aList = [1, 2, 3, 4, 5]
#idx1, idx2 = 1,2

#print(swap(aList, idx2, idx1))


#INDEXOFMIN

#aList = [1, 3, 2, 4, 6]


def indexOfMin(aList):
    minIndex = 0
    #ADD A COUNTER
    for i, element in enumerate(aList):
        if element < aList[minIndex]:
            minIndex = i
    return minIndex


