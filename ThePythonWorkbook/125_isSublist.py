import unittest

def isSublist(smaller, larger):
    if smaller == []:
        return True
    for index in range(len(larger)):
        if larger[index] in smaller:
            for i in range(len(smaller)):
                if larger[index + i] not in smaller:
                    return False
            return True


class Unittests(unittest.TestCase):

    def testNotAdjacentElements(self):
        smaller = [2, 4]
        larger = [1, 2, 3, 4]
        self.assertFalse(isSublist(smaller, larger))

    def testHalfListInMiddle(self):
        smaller = [2, 3]
        larger = [1, 2, 3, 4]
        self.assertTrue(isSublist(smaller, larger))

    def testAllSingleElements(self):
        smaller = [2]
        larger = [2, 3, 4, 5]
        self.assertTrue(isSublist(smaller, larger))

        smaller = [3]
        self.assertTrue(isSublist(smaller, larger))

        smaller = [4]
        self.assertTrue(isSublist(smaller, larger))

        smaller = [5]
        self.assertTrue(isSublist(smaller, larger))

    def testEmptySmallerList(self):
        smaller = []
        larger = [1, 2, 3, 4]
        self.assertTrue(isSublist(smaller, larger))

    def testBothEmptyLists(self):
        smaller = []
        larger = []
        self.assertTrue(isSublist(smaller, larger))

if __name__ == '__main__':
    unittest.main()
