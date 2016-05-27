def main():
  word = input("type a word: ")
  listOfWords = [word]
  while word != '':
    word = input("type a word: ")
    listOfWords.append(word)
  for element in listOfWords:
    print(element)
  removeDuplicates(listOfWords)

def removeDuplicates(list):
  seen = []
  unique = []
  for element in list:
    if element not in seen:
      unique.append(element)
      seen.append(element)
  for element in unique:
    print(element)

if __name__ == '__main__':
    main()