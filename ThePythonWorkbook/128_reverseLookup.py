# reverse lookup method should return all keys in a dictionary that map to
# a specific value

def key_value_gen(k):
    yield (k)
    yield chr(k % 26 + 65)

def reverseLookup(d, value):
    keyList = []
    for k, v in d.items():
        if v == value:
            keyList.append(k)
    return keyList

def main():
    d = dict(map(key_value_gen, range(500)))
    keys = reverseLookup(d, 'A')
    print("all keys for 'A': ", keys)

if __name__ == '__main__':
    main()
