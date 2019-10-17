
# Client: GameEnv

#
# PURPOSE:
# A simple container for storing the values 'num_rows', 'num_cols',
# 'player_id', and 'grid'
#
# PARAMETERS:
# num_rows: The number of rows in the grid
# num_cols: The number of columns in the grid
# player_id: The ID of the player (a string, which will be displayed
# in the grid)
# grid: The game board (a 2D array of characters, representing
# players, treasures, and blank spaces)
#
# RETURN/SIDE EFFECTS:
# N/A
#
# NOTES:
# N/A
#
class Game_Env:
	def __init__(self, num_rows, num_cols, player_id, grid):
		self.num_rows = num_rows
		self.num_cols = num_cols
		self.player_id = player_id
		self.grid = grid

# displayGrid
#
# PURPOSE:
# Displays the grid contained in 'game_env.grid' on the screen
#
# PARAMETERS:
# stdscr: Must be a reference to a valid curses screen
# game_env: Contains a valid game environment
#
# RETURN/SIDE EFFECTS:
# N/A
#
# NOTES:
# N/A
#
def displayGrid(stdscr, game_env):
	stdscr.clear()
	pos = 0
	for row in range(game_env.num_rows):
		for col in range(game_env.num_cols):
			stdscr.addstr(row, col * SPACER, game_env.grid[pos])
			pos = pos + 1
	stdscr.refresh()
	
# Client: Main Loop
#
# PURPOSE:
# This is the main loop for the client. It initially receives 'num_rows',
# 'num_cols', 'player_id', and 'grid' from the server. That grid is then
# displayed on the curses screen. Then, repeatedly, the client will wait
# for a message from the server, either to grant the current Player a turn,
# or to display the updated game board on the screen. If the Player is
# granted a turn, this loop will wait for a character input and then send
# that to the server.
#
# PARAMETERS:
# stdscr: Must be a reference to a valid curses screen
#
# RETURN/SIDE EFFECTS:
# N/A
#
# NOTES:
# Multiple character inputs will be buffered and transmitted at the rate of
# one character per Player turn. If the server rejects a move for being
# invalid, the Player will lose a turn.
# Exceptions will be caught and logged, and result in the orderly termination
# of this function.
#

def main(stdscr):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		sock.connect((HOST, PORT))
		sock.sendall(ics226.HELLO)
		
		reply = ics226.getBuf(sock, 1)
		num_rows = struct.unpack('!B', reply)[0]
		
		reply = ics226.getBuf(sock, 1)
		num_cols = struct.unpack('!B', reply)[0]
		
		reply = ics226.getBuf(sock, 1)
		player_id = struct.unpack('!B', reply)[0]
		
		reply = ics226.getBuf(sock, num_rows * num_cols)
		grid = reply.decode('utf-8')
		
		game_env = Game_Env(num_rows, num_cols, str(player_id), grid)
		
		displayGrid(stdscr, game_env)
		logger.debug(game_env.player_id + ' is ready')
		while True:
			data = ics226.getBuf(sock, 1)
			if data == ics226.GO:
				logger.debug(game_env.player_id + ' going ahead')
				displayGrid(stdscr, game_env)
				k = stdscr.getkey()
				sock.sendall(k.encode('utf-8'))
			elif data == ics226.GRID:
				logger.debug(game_env.player_id + ' got grid')
				reply = ics226.getBuf(sock, num_rows * num_cols)
				game_env.grid = reply.decode('utf-8')
				displayGrid(stdscr, game_env)
			elif data == ics226.QUIT:
				logger.debug(game_env.player_id + ' is quitting')
				break
	except Exception as e:
		logger.critical(str(e), exc_info = 1)
		
	sock.close()
	logger = logging.getLogger('client.py')
	logger.setLevel(logging.DEBUG)
	handler = logging.handlers.SysLogHandler(address = '/dev/log')
	logger.addHandler(handler)
	
	curses.wrapper(main)