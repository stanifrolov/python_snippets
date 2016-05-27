def main():
  number = int(input("give number - 0 for end: "))
  listOfNumbers =  [number]
  while number != 0:
    number = int(input("give number - 0 for end: "))
    listOfNumbers.append(number)
  print(sorted(listOfNumbers))

if __name__ == '__main__':
    main()