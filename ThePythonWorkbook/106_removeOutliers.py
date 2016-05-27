def main():
  number = int(input("give number - 0 for end: "))
  listOfNumbers =  [number]
  while number != 0:
    number = int(input("give number - 0 for end: "))
    listOfNumbers.append(number)
  listOfNumbers.remove(0)
  numberOfExtremesToRemove = int(input("give number of extremes to remove: "))
  removeOutliers(listOfNumbers, numberOfExtremesToRemove)

def removeOutliers(listOfElements, n):
  copy = list(listOfElements)
  for i in range(n):
    copy.remove(max(copy))
    copy.remove(min(copy))
  print(copy)
  print(listOfElements)

if __name__ == '__main__':
    main()