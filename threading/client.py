# client
import socket
import sys
import curses

def direction():

	inputKey = 0
	try:
		while True:
			char = getch()
			if char == ord('q'):
				break
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
	finally:
		return inputKey

def main():
	soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = "127.0.0.1"
	port = 8888

	try:
		soc.connect((host, port))
	except:
		print("Connection error")
		sys.exit()

	print("Enter 'quit' to exit")
	
	message = input(" -> ")

	while message != 'quit':
		
		soc.sendall(message.encode("utf8"))
		if soc.recv(5120).decode("utf8") == "-":
			pass        # null operation

		message = input(" -> ")

	soc.send(b'--quit--')
	

if __name__ == "__main__":
	main()