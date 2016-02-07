# 8 Widgets and Gizmos

def computeTotalWeight(widgets, gizmos):
	return (widgets*75) + (gizmos*112)

import unittest

class TestTotal(unittest.TestCase):
	
	def testTheNumberSeven(self):
		widgets = 2
		gizmos = 1
		self.assertEqual(computeTotalWeight(2,1), 150+112)


if __name__ == '__main__':
	unittest.main()