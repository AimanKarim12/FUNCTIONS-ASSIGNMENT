
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
  for el in aList:
    if el == item:
      return True
  return False

print("INDEX OF ASSIGNMENT") 
#LETTER IS ON LIST
aList = ['A', 'B', 'C', 'D']
selected = 'C'
#LETTER IS NOT ON LIST 
list = ['A', 'B', 'C', 'D']
selected2 = 'Z'

def indexOf():
  if indexof(aList, selected):
    print(f"Letter is found on list: {selected}")
  else:
    print("Letter is not on list")

  if indexof(list, selected2):
    print("Letter is found")
  else:
    print("Letter is not on list")
indexOf()

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
aList = [4, 3, 2, 1]

print("INDEX OF MIN ASSIGNMENT")

def indexmin():
  print(min(aList))
indexmin()

def indexmin():
  print(min(aList))
indexmin()
