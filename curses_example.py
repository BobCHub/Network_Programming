import curses
import random
import time
import sys
import select
import textwrap

def getNewBoard():	
	# Create a new 20x10 board data structure.
	board = []
	board.append([])
	for x in range(20): # The main list is a list of 20 lists.
		board.append([])
		
		for y in range(10): # Each list in the main list has 10 single-character strings.
			
			# Use different characters for the space dollar sign treasue.
			if random.randint(0, 5) == 1 | 2:
				
				board[x].append(' $' )

			else:
				board[x].append(' _')		
	# The map is a 2D list filled with players 'X and Y'	
	board[0][0] = ' X'
	board[19][9] = ' Y'	
	return board
	
# The map is a 2D list filled with '- and $'
def drawBoard(board):
	# Print each of the 10 rows.
	theBoard =[]
	for row in range(10):
		# Single-digit numbers need to be padded with an extra space.
		if row < 10:
			extraSpace = '    '
		# Create the string for this row on the board.
		boardRow = ''
		for column in range(20):
			boardRow += board[column][row]
			
		theBoard = ('%s' % ( boardRow))
		return theBoard
		

screen = curses.initscr()
curses.noecho()
curses.cbreak()
curses.start_color()
screen.keypad( 1 )    # delete this line
curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_CYAN)
highlightText = curses.color_pair( 1 )
normalText = curses.A_NORMAL
screen.border( 0 )
curses.curs_set( 0 )

box = curses.newwin(10, 50, 10, 50)




	
box.keypad( 1 )
box.box()
box.addstr(3, 3, "YOU HAVE PRESSED: ")
board = getNewBoard()

box.addstr(5, 3, textwrap.fill(drawBoard(board)))




box.refresh()

x = box.getch()
while x != 27:
	box.erase()
	if x == ord('q'):
		break
	elif x == curses.KEY_RIGHT:
		inputKey = x
		box.addstr( 3, 3, "YOU HAVE PRESSED: " + str(inputKey) )
		# pos[0] += 1
	elif x == curses.KEY_LEFT:
		inputKey = x
		box.addstr( 3, 3, "YOU HAVE PRESSED: " + str(inputKey) )     
		# pos[0] -= 1
	elif x == curses.KEY_UP: # Up arrow
		inputKey = x
		box.addstr( 3, 3, "YOU HAVE PRESSED: " + str(inputKey) )   
		# pos[1] -= 1  
	elif x == curses.KEY_DOWN: # Down arrow
		inputKey = x
		box.addstr( 3, 3, "YOU HAVE PRESSED: " + str(inputKey) )
		# pos[1] += 1
	else :
		box.addstr( 3, 3, "Not a Direction Arrow Please try Again " )
	
	
	box.addstr(5, 3, textwrap.fill(drawBoard(board)))
	screen.border( 0 )
	box.border( 0 )
	screen.refresh()  # delete this line
	box.refresh()     # delete this line
	x = box.getch()

curses.endwin()
exit()

