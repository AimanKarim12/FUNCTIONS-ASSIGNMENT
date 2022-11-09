#FUNCTIONS ASSIGNMENT

#CONTAINS
def contains(aList, item):
  for el in aList:
    if el == item:
      return True
  return False

print("CONTAINS ASSIGNMENT")
print(contains([1, 2, 3, 4], 2))
print(contains([1, 2, 3, 4], 5))

#INDEXOF 
def indexof(aList, item):
  for [i] in range(len(aList)):
    if [i] == item:
      return True
  return False

print (aList[i])
#REVERSE
aList = [1, 2, 3, 4]

def reverse(values):
    return values[::-1]

print("REVERSE ASSIGNMENT")
print(reverse(aList))

#SWAP
aList = [1, 2, 3, 4]

def swap():
  index1, index2 = 2, 3

  before, after = aList.index(index1), aList.index(index2)

  aList[before], aList[after] = aList[after], aList[before]
swap()

print("SWAP ASSIGNMENT")
print(aList)

#INDEXOFMIN
def indexofmin(array, x):

	minpos = array.index(min(array))

	print ("position of minimum at", minpos + 1)

array = [4, 3, 2, 1]
indexofmin(array, len(array))



