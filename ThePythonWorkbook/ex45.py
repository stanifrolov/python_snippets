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
	print('   ', 0,  '  ', 1,  '  ', 2,  '  ', 3,  '  ', 4,  '  ', 5,  '  ', 6,  '  ', 7)
	for i in range(len(board)):
		print(i, board[i])

def getIndex(board, row, element):
	print(row, element, 'is', board[row][element])

chessBoard = createBoard(8)
printBoard(chessBoard)
row = int(input("Which row do you wanna know? "))
element = int(input("Which element do you wanna know? "))
getIndex(chessBoard, row, element)