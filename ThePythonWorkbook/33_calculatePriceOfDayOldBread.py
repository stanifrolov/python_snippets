#33 Day Old Bread
loave = 3.49
discountPerDay = 0.6

numberOfLoaves = int(input("how many do you want to buy? "))

def calcPrice():
    originalPrice = numberOfLoaves * loave;
    discountPrice = originalPrice * discountPerDay;
    print("original %.2f:  but today %.2f" % (originalPrice, discountPrice))


calcPrice()