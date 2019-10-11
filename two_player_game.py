from random import randint, choice
import subprocess
import platform
import time


# Board Grid movement 
class MapGrid:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.walls = []
		self.startX = (0, 0)
		self.startY= (19, 9)
		self.goalX = (width-1, height-1)
		self.goalY = (width-1, height-1)
		self.player1 = (0, 0)
		self.player2 = (19, 9)
    
	# Player 1 movement function
	def move_player1(self, d):
		x = self.player1[0]
		y = self.player1[1]
		pos = None
		# Move player with in the array grid according to key input
		if d[0] == 'r':
			pos = (x + 1, y)
		if d[0] == 'l':
			pos = (x - 1, y)
		if d[0] == 'u':
			pos = (x, y - 1)
		if d[0] == 'd':
			pos = (x, y + 1)
		col,row = pos
		if row >=0 and col >=0 and row <=9 and col <=19 and pos not in self.walls:
			
			self.player1 = pos
			print(str(2), pos)
		if pos == self.goalX:
			print("You made it to the end!")
	
	# Player 2 movement function
	def move_player2(self, d):
			x = self.player2[0]
			y = self.player2[1]
			pos = None
			
			'''
			# Constant Values for keyboard input from curses
			L = 37
			R = 39
			U = 38
			D = 40
			
			'\x1b[A' = up
			'\x1b[B'= down
			'\x1b[C' = right
			\x1b[D'= left
			
			'''
			
			if d[0] == 'r':
				pos = (x + 1, y)
			if d[0] == 'l':         
				pos = (x - 1, y)
			if d[0] == 'u':
				pos = (x, y - 1)
			if d[0] == 'd':
				pos = (x, y + 1)
			col,row = pos
			if row >=0 and col >=0 and row <=9 and col <=19 and pos not in self.walls:
				
				self.player2 = pos
				print(str(2), pos)
			if pos == self.goalY:
				print("You made it to the end!") # screen.addstr(0, 0, "You made it to the end!")

# draw the grid and placing the symbols 
def draw_grid(g, width=3):
	for y in range(g.height):
		for x in range(g.width):
			if (x, y) in g.walls:
				symbol = '$'
			elif (x, y) == g.player1:
				symbol = 'X'
			elif (x, y) == g.player2:
				symbol = 'Y'
			elif (x, y) == g.startX:
				symbol = '<'
			elif (x, y) == g.goalX:
				symbol = '>'
			elif (x, y) == g.startY:
				symbol = '<'
			elif (x, y) == g.goalY:
				symbol = '>'
			else:
				symbol = '_'
				
				
				
			# TO DO: NEED TO PRINT USES CURSES
			print("%%-%ds" % width % symbol, end="") # screen.addstr(0, 0, "You made it to the end!")
		print()
		
		
		
		

# Distribute the Tresure through out the grid randomly
def get_treasure(g: MapGrid, pct=.05) -> list:
		out = []
		for i in range(int(g.height*g.width*pct)//2):
			# Randomizer
			x = randint(1, g.width-2)
			y = randint(1, g.height-2)
			out.append((x, y))
			# choice() returns a random item from list.
			out.append((x + choice([-1, 0, 1]), y + choice([-1, 0, 1])))
		return out


# clear() method removes all items from the dictionary
def clear():
	subprocess.Popen("cls" if platform.system() == "Windows" else "clear", shell=True)
	time.sleep(.01)


def main():
	g = MapGrid(20, 10)
	g.walls = get_treasure(g)
	playerOneTurn = True
	winner = False
	

	while not winner :
		draw_grid(g)  
		
		
		'''
		# Send
		import pickle
		
		x = draw_grid(g)
		print(x)
		grid = pickle.dumps(x)
		s.send(grid)
		
		# Recieve 
		import pickle
		
		grid = pickle.loads(tcp_recieve())
		print(grid)

		'''

		if playerOneTurn :
			print( "Player 1:") # screen.addstr(0, 0, "Player 1:")
			try:
				# d = inputKey
				d = input("Which way? (r, l, u, d)")  # screen.addstr(1, 0, "Which way? (r, l, u, d)")
				g.move_player1(d)
				if g.player1 != g.goalX:
					playerOneTurn = False
				else:
					winner = True	
			except:
				print("please enter a valid field") # screen.addstr(0, 0, "please enter a valid field")
		else :
			print( "Player 2:")
			try:
				# d = inputKey
				d = input("Which way? (r, l, u, d)") # screen.addstr(1, 0, "Which way? (r, l, u, d)")
				g.move_player2(d)
				if g.player2 != g.goalY:
					playerOneTurn = True
				else:
					winner = True
			except:
				print("please enter a valid field") # screen.addstr(3, 0, "please enter a valid field")

if __name__ == '__main__':
	main()
	
	




