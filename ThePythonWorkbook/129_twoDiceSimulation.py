from random import randint

def key_value_gen(k):
    yield (k)
    yield 0

def twoDiceSimulation():
    d = dict(map(key_value_gen, range(1, 13)))
    for i in range(1, 1000):
        diceOne = randint(1, 6)
        diceTwo = randint(1, 6)
        sum = diceOne + diceTwo
        d[sum] = d[sum] + 1
    return d



def main():
    d = twoDiceSimulation()
    for element in d:
        print(element, ':', d[element])

if __name__ == '__main__':
    main()