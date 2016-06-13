import unittest
from random import randint

def getPrimeNumbers(limit):
    numbers = []
    numbers.extend(range(2, limit + 1))
    p = 2
    while p < limit:
        multiples = [x for x in range(p + 1, limit + 1) if x % p == 0]
        for element in multiples:
            if element in numbers:
                index = numbers.index(element)
                numbers[index] = 0
        indexForNextNonZeroElement = getNextNonZero(numbers, p)
        nextNonZeroElement = numbers[indexForNextNonZeroElement]
        if nextNonZeroElement > p:
            p = nextNonZeroElement
        else:
            p = p + 1
    numbers = [element for element in numbers if element != 0]
    return numbers


def getNextNonZero(list, old):
    return next((index for index, x in enumerate(list) if x != 0 and x != old), None)

class Unittest(unittest.TestCase):

    def testGetNextNonZero(self):
        list = [1, 0, 2]
        nextNonZero = getNextNonZero(list, 1)
        self.assertEqual(2, nextNonZero)

    def testRandomDivisionOfLargeFoundPrimeNumber(self):
        limit = 100
        foundPrimes = getPrimeNumbers(limit)
        maxFoundPrime = max(foundPrimes)
        randomDivisor = randint(2, maxFoundPrime - 1)
        self.assertTrue(maxFoundPrime % randomDivisor != 0)

    def testPrimeNumbersUntil_50(self):
        limit = 50
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        foundPrimes = getPrimeNumbers(limit)
        self.assertEqual(foundPrimes, primes)

    def testPrimeNumbersUntil_40(self):
        limit = 40
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
        foundPrimes = getPrimeNumbers(limit)
        self.assertEqual(foundPrimes, primes)

    def testPrimeNumbersUntil_20(self):
        limit = 20
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        foundPrimes = getPrimeNumbers(limit)
        self.assertEqual(foundPrimes, primes)

    def testPrimeNumbersUntil_3(self):
        limit = 3
        primes = [2, 3]
        foundPrimes = getPrimeNumbers(limit)
        self.assertEqual(foundPrimes, primes)

    def testPrimeNumbersUntil_2(self):
        limit = 2
        primes = [2]
        foundPrimes = getPrimeNumbers(limit)
        self.assertEqual(foundPrimes, primes)

    def testPrimeNumbersUntil_1(self):
        limit = 1
        primes = []
        foundPrimes = getPrimeNumbers(limit)
        self.assertEqual(foundPrimes, primes)

if __name__ == '__main__':
    unittest.main()