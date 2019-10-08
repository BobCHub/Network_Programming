import curses
import random
import time
import sys
import select

def getNewBoard():
	
	# Create a new 20x10 board data structure.
	board = []
	board.append([])
	
	
	for x in range(20): # The main list is a list of 20 lists.
		board.append([])
		
		for y in range(10): # Each list in the main list has 10 single-character strings.
			
			# Use different characters for the space dollar sign treasue.
			if random.randint(0, 20) == 1 | 2:
				
				board[x].append(' $' )

			else:
				board[x].append(' _')
				
	board[0][0] = ' X'
	board[19][9] = ' Y'	

	return board
	
def drawBoard(board):

	# Print each of the 10 rows.
	for row in range(10):
		# Single-digit numbers need to be padded with an extra space.
		if row < 10:
			extraSpace = '    '

		# Create the string for this row on the board.
		boardRow = ''
		for column in range(20):
			boardRow += board[column][row]
			
		theBoard = ('%s' % ( boardRow))
		
		print(theBoard)
		
		
	
def main():
		
		board = getNewBoard()
		drawBoard(board)

		
		

if __name__=='__main__':
		main()