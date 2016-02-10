# Scan a string message and capitalize some characters like 'i' into 'I' and
# beginning character after a ending sentence.

# Rule 1: 'i' -> 'I'
# Rule 2: first character of string
# Rule 3: first non-space character after '.', '!', '?'

import unittest

def capitalizeSentence(string):
    words = string.split()
    # Rule 2
    words[0] = words[0].capitalize()
    for i in range(len(words)):
        # Rule 1
        if words[i] == 'i':
            words[i] = 'I'
        # Rule 3
        if (i+1 < len(words)) and ('!' in words[i] or '?' in words[i] or '.' in words[i]):
            words[i+1] = words[i+1].capitalize()
    return(words)

def main():
    string = input("Give your sentence: ")
    capitalizeSentence(string)

class testString(unittest.TestCase):
    def testAllEndCharacters(self):
        correctSentence = ['I', 'want', 'it!', 'Yes?', 'Aha.']
        self.assertEqual(capitalizeSentence('i want it! yes? aha.'), correctSentence)

if __name__ == '__main__':
    unittest.main()