import unittest
import random

def main():
  print(createDeck())
  print(shuffle(createDeck()))

def shuffle(listOfElements):
    for element in listOfElements:
        randomIndexOne = random.randint(0, 51)
        randomIndexTwo = random.randint(0, 51)
        temp = listOfElements[randomIndexOne]
        listOfElements[randomIndexOne] = listOfElements[randomIndexTwo]
        listOfElements[randomIndexTwo] = temp
    return listOfElements

def createDeck():
    listOfCards = []
    cardValues = [1, 2, 3, 4, 5, 6, 8, 9, 'T', 'J', 'Q', 'K', 'A']
    cardSuits = ['s', 'h', 'd', 'c']
    for valueOfCard in cardValues:
        for cardSuit in cardSuits:
            listOfCards.append(str(valueOfCard) + cardSuit)
    return listOfCards

class UnitTests(unittest.TestCase):

    def testSizeOfCreatedCardList(self):
        self.assertEqual(len(createDeck()), 52)

if __name__ == '__main__':
    main()