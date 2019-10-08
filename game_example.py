from random import randint, choice
import subprocess
import platform
import time


class MapGrid:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.walls = []
		self.start = (0, 0)
		self.goal = (width-1, height-1)
		self.player = (0, 0)

	def move_player(self, d):
		x = self.player[0]
		y = self.player[1]
		pos = None

		if d[0] == 'r':
			pos = (x + 1, y)
		if d[0] == 'l':
			pos = (x - 1, y)
		if d[0] == 'u':
			pos = (x, y - 1)
		if d[0] == 'd':
			pos = (x, y + 1)

		if pos not in self.walls:
			self.player = pos

		if pos == self.goal:
			print("You made it to the end!")


def draw_grid(g, width=3):
	for y in range(g.height):
		for x in range(g.width):
			if (x, y) in g.walls:
				symbol = '$'
			elif (x, y) == g.player:
				symbol = 'X'
			elif (x, y) == g.start:
				symbol = '<'
			elif (x, y) == g.goal:
				symbol = '>'
			else:
				symbol = '_'
			print("%%-%ds" % width % symbol, end="")
		print()


def get_treasure(g: MapGrid, pct=.10) -> list:
		out = []
		for i in range(int(g.height*g.width*pct)//2):

			x = randint(1, g.width-2)
			y = randint(1, g.height-2)

			out.append((x, y))
			out.append((x + choice([-1, 0, 1]), y + choice([-1, 0, 1])))
		return out


def clear():
	subprocess.Popen("cls" if platform.system() == "Windows" else "clear", shell=True)
	time.sleep(.01)


def main():
	g = MapGrid(20, 10)
	g.walls = get_treasure(g)

	while g.player != g.goal:
		draw_grid(g)
		d = input("Which way? (r, l, u, d)")
		g.move_player(d)
		clear()
	print("You made it!")


if __name__ == '__main__':
	main()