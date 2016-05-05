polynom = "7x^12-2x^9+9x^3-6x^2+2x+8"

print "the given polynom is: %s" % polynom

# generates a list of the single summands for positive summands only
# ToDo: split not only at '+' but also at '-'

"""
        list.pop(index) - removes element at index position from list and returns it
        list.remove(element) - removes element if it is found in list
        del(list[index]) - removes elemnt at index position just as .pop but does not return it
	to modify list elements use loop  and index as:
		for i in range(len(list)):
			do something
	otherwise easily loop through list by:
		for element in list:
			do something
	make list from list_of_lists by the flatten function as:
	def flatten(lists):
		results =[]
		for numbers in lists:
			for element in numbers:
				results.append(element)
		return results
	to keep printing on the samle line use trailing comma - print something,
"""

split_minus = polynom.split('-')
splitted = []

for x in range(0, len(split_minus)):
        a = split_minus[x].split('+')
print split_minus
print a

"""
    need to split again at the '^" and generate coeffizient and exponent for each summand and fill up a dictioanry like
    polynom_dict = {
        exponent : coeffizient,
        ...
    }
"""