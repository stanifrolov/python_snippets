# 79 Simulate 100 random numbers. Take first number as maximum value.
# For every next number that is larger update the value.


import random

maxValue = 0
count = 0
countOfUpdates = 0
while(count <= 100):
    randomNumber = random.uniform(0,100)
    if randomNumber > maxValue:
        maxValue = randomNumber
        countOfUpdates += 1
        print(randomNumber, "<--- UPDATE")
    else:
        print(randomNumber)
    count += 1

print("Maximum value is ", maxValue)
print(countOfUpdates, "updates has happened in this simulation.")