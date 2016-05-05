lst = [0,2,4,3,2,2,2,1]

def count(sequence, item):
    count = 0
    for element in sequence:
        print "item is ", element
        print "element is " , item
        if element == item:
            count += 1
    return count

print count(lst,2)