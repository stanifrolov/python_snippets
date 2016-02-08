# compute even parity bit for a byte = total bits have to be even

import unittest

def computePartityBit(byte):
    parityBit = 0
    count = 0
    for bit in byte:
        if bit == '1':
            count +=1

    if count % 2:
        parityBit = 1

    print("parity bit has to be ", parityBit, 'for even partiy.')
    return parityBit

byte = input("Please give a byte: ")
computePartityBit(byte)

class TestParity(unittest.TestCase):

	def testByte(self):
		correctParityBit = 0
		self.assertEqual(computePartityBit('11111111'), correctParityBit)

if __name__ == '__main__':
	unittest.main()