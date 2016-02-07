#45 What Color is that Square

def createBoard(order):

	# create 2x2 matrix and fill with zeros
	gameBoard = [[0 for j in range(order)] for i in range(order)]

	# looping through all elements
	for i in range(len(gameBoard)):
		for j in range(len(gameBoard[i])):
			if i%2:
				if j%2:
					gameBoard[i][j] = 'X'
				else: 
					gameBoard[i][j] = '0'
			else:
				if j%2:
					gameBoard[i][j] = '0'
				else:
					gameBoard[i][j] = 'X'
	return gameBoard

def printBoard(board):
	print('   ', 'A',  '  ', 'B',  '  ', 'C',  '  ', 'D',  '  ', 'E',  '  ', 'F',  '  ', 'G',  '  ', 'H')
	for i in range(len(board)):
		print(i, board[i])

def equivalentNumber(string):
	equivalent = {
		'A' : 0,
		'B' : 1,
		'C' : 2,
		'D' : 3,
		'E' : 4,
		'F' : 5,
		'G' : 6,
		'H' : 7,
	}
	return equivalent[string]

def getField(fieldOfInterest, board, row, column):
	print(fieldOfInterest, 'is', board[row][column])

def getRowAndColumn(string):
	column, row = string
	return (column, row)

chessBoard = createBoard(8)
printBoard(chessBoard)
fieldOfInterst = input("Which field do you want to know? ")

column, row = getRowAndColumn(fieldOfInterst)
row =  int(row)
columnNumber = equivalentNumber(column)
getField(fieldOfInterst, chessBoard, row, columnNumber)


