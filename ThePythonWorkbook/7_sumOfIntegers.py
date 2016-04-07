# 7 Sum of the first n positive integers
# Write a program that reads a positive integer, n, from the user and then displays the
# sum of all of the integers from 1 to n. The sum of the first n positive integers can be
# computed using the formula: sum = ((n)n+1)/2

# test github

import unittest

x = 7

def sum(n):
	return ((n*(n+1))/2)

class TestSum(unittest.TestCase):

	def testTheNumberSeven(self):
		correctSum = 7+6+5+4+3+2+1
		self.assertEqual(int(sum(7)), correctSum)


if __name__ == '__main__':
	unittest.main()
