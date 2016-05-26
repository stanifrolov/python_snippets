import unittest

def main():
    date = input('Type date in DD/MM/YYYY as e.g. 10/06/1990 for June 10, 1990: ')
    isMagicDate(date)
    findNumberOfMagicDates(2000)

def isMagicDate(date):
    day, month, year = date.split('/')
    day = int(day)
    month = int(month)
    year = int(year)
    decade = year % 100
    magic = day * month
    if magic == decade:
         return True
    else:
         return False

def findNumberOfMagicDates(millenium):
    # NOTE: different day numbers in months is not taken care of
    numberOfMagicDates = 0
    for year in range(millenium, millenium + 1000):
        for month in range(1, 12):
            for day in range(1, 31):
                date = str(day) + '/' + str(month) + '/' + str(year)
                if isMagicDate(date):
                    numberOfMagicDates = numberOfMagicDates + 1
    print(numberOfMagicDates)

class Tests(unittest.TestCase):

    def testYears(self):
        self.assertEqual(isMagicDate('10/06/1960'), True)

if __name__ == '__main__':
    main()