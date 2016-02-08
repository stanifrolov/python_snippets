# factorize an integer in prime numbers

def factorize():
    n = int(input("give a number larger than 2: "))
    number = n
    factor = 2
    factors = []
    while (factor <= number):
        if number % factor == 0:
            factors.append(factor)
            number = number / factor
        else:
            factor += 1
    print("prime factors of ", n, "are: ")
    for factors in factors:
        print(factors)

factorize()