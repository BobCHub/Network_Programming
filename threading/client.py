# client
#!/usr/bin/python3

import socket
import sys
import curses
import struct

def direction(screen):

	inputKey = 0
	
	while True:
		char = screen.getch()
		if char == ord('q'):
			return "q"
		elif char == curses.KEY_RIGHT:
			inputKey = char
			return inputKey
		elif char == curses.KEY_LEFT:
			inputKey = char
			return inputKey    
		elif char == curses.KEY_UP:
			inputKey = char
			return inputKey     
		elif char == curses.KEY_DOWN:
			inputKey = char
			return inputKey

	return inputKey

def main():
	soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = "10.51.11.20"
	port = 12345

	screen = curses.initscr()
	curses.noecho()
	screen.keypad(True)
	char = direction(screen)
	try:
		soc.connect((host, port))
	except:
		print("Connection error")
		sys.exit()
	while( char != "q"): 
		

		screen.addstr(0,0,"Enter 'quit' to exit")
		
		# message = char
		screen.addstr(1,0,str(char))
	
		soc.sendall(struct.pack('!H', char))
		char = direction(screen)
		# message = char

		#soc.send(b'--quit--')
		
	screen.endwin()
if __name__ == "__main__":
	main()
