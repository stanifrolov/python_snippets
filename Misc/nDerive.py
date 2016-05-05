# this is a script to calculate the derivation of a polynom with non negativ exponents
# input = raw_input()
input = {
	0 : 9,
	1 : 2,
	2 : 4,
	4 : 7,
}

output = {}

def nDerive(input):
	for x in input:
		if x < 0:
			print "only non-negativ exponents allowed"
			return False
		elif x == 0:
			y = 0
		else:
			y = x - 1
		output[y] = input[x] * x

	print "the derivation of: %s is: %s:" % (input, output)
	return True

nDerive(input)

