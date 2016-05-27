def main():
  number = int(input("give number - 0 for end: "))
  listOfNumbers =  [number]
  while number != 0:
    number = int(input("give number - 0 for end: "))
    listOfNumbers.append(number)
  listOfNumbers.remove(0)
  listOfNumbers = sorted(listOfNumbers)
  listOfNumbers = reversed(listOfNumbers)
  for element in listOfNumbers:
    print(element)

if __name__ == '__main__':
    main()