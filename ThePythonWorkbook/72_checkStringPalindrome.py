# 72 check a given string for being a palindrome

import unittest

def checkStringForPalindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

stringToCheck = input("Please give a string to check: ")
print(checkStringForPalindrome(stringToCheck))

class TestPalindromFunction(unittest.TestCase):
    def testString(self):
        self.assertEqual(checkStringForPalindrome('hannah'), True)

if __name__ == '__main__':
    unittest.main()

