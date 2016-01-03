# 32 Sort 3 Integers
import unittest

def sortThreeIntegers(a,b,c):
    # a,b,c = map(int,input().split())
    aList = [a, b, c]
    maxValue = max(aList)
    minValue = min(aList)
    newList = aList
    newList.remove(maxValue)
    newList.remove(minValue)
    middle = newList[0]
    result = [minValue, middle, maxValue]
    return result

class TestSortedList(unittest.TestCase):

	def testListForBeingEqual(self):
		correctList = [1,2,3]
		self.assertEqual(sortThreeIntegers(3,2,1), correctList)

if __name__ == '__main__':
	unittest.main()

