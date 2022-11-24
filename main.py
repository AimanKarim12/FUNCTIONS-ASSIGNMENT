#FUNCTIONS ASSIGNMENT

#CONTAINS
def contains(aList, item):
  for el in aList:
    if el == item:
      return True
  return False

#INDEXOF 
#def indexof(aList, item):
#  for [i] in range(len(aList)):
#    if [i] == item:
#      return True
#  return False

#REVERSE
#def reverse(list):

#    i = 1
#    for value in list:
#       reversed.append(list[len(list) - i])
#    i += 1
#    return reversed

#SWAP
#def swap(aList, idx1, idx2):
#  aList[idx1], aList[idx2] = aList[idx2], aList[idx1]
#  return aList

#aList = [1, 2, 3, 4, 5]
#idx1, idx2 = 1,2

#print(swap(aList, idx2, idx1))


#INDEXOFMIN

#aList = [1, 3, 2, 4, 6]


#def indexOfMin(aList, x):
#    mvalue = aList[0]
#    mindex = 0
#    for i in range(1, x):
#      if (aList[i] < mvalue):
#        mvalue = aList[i]
#        mindex = i
      
#    return mindex


