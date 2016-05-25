import unittest

def main():
    string = input("Type in something. I will decide if it is an integer: ")
    isInteger(string)

def isInteger(string):
    # at least one digit
    # only digits
    # leading +/- allowed

    if not string:
        return False

    if str.startswith(string, ' '):
        string = str.lstrip(string)

    if str.endswith(string, ' '):
        string = str.rstrip(string)

    if str.startswith(string, '+'):
        string = str.lstrip(string, '+')

    if str.startswith(string, '-'):
        string = str.lstrip(string, '-')

    for character in string:
        if not str.isdigit(character):
            return False

    return True

class testString(unittest.TestCase):

    def testStartWithWhiteSpace(self):
        string = ' 123'
        self.assertEqual(isInteger(string), True)

    def testEndWithWhiteSpace(self):
        string = '123 '
        self.assertEqual(isInteger(string), True)

    def testStartWithPlus(self):
        string = '+123'
        self.assertEqual(isInteger(string), True)

    def testStartWithMinus(self):
        string = '-123'
        self.assertEqual(isInteger(string), True)

    def testCharacterString(self):
        string = 'abc'
        self.assertEqual(isInteger(string), False)

    def testCharInbetweenDigits(self):
        string = '123a123'
        self.assertEqual(isInteger(string), False)

    def testInbetweenWhiteSpace(self):
        string = '12 34'
        self.assertEqual(isInteger(string), False)

    def testEmptyString(self):
        string = ''
        self.assertEqual(isInteger(string), False)

if __name__ == '__main__':
    unittest.main()