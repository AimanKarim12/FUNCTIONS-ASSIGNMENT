#FUNCTIONS ASSIGNMENT

#CONTAINS
def contains(aList, item):
  for el in aList:
    if el == item:
      return True
  return False

#INDEXOF 
aList = [1, 3 , 4, 6]
item = 3

def indexof(aList, item):
  for i in range(len(aList)):
    if [i] == item:
      return i
  return -1
print(indexof)

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


def indexOfMin(aList):
    mindex = 0
    for i in range(1, len(aList)):
      if (aList[i] < mvalue):
        mvalue = aList[i]
        mindex = i
      
    return mindex

aList = [2, 1 , 4, 5]

print(indexOfMin)



