import time
import random
import os

DEAD = 0
ALIVE = 1

def dead_state(w,h):

	return [[DEAD]*w]*h

def random_state(w,h):

	state = dead_state(w,h)
	random_state = []
	
	for i in state:
		random_state.append([random.randint(0,1) for l in range(0, len(i))])
			
	return random_state

def render(s,c):
		
	a = u"\u2588"
	d = ' '
	r = []
	
	for q in s: #in each item of grid (another list)

		r.append([d if j == DEAD else a for j in q]) #in each of those list-items, set character if 0 or 1 and append
	
	rendered_state = '\n'.join(str(e) for e in r).replace(',',' ').replace('[','|').replace(']','|').replace('\'' ,'') #ugly AF but I can understand it, cleaning up grid

	print(f'\033[{c}m {3*d*len(s[0])}\n{rendered_state}\n{3*d*len(s[0])}\033[00m') #format string with ansii color, padding, state....


def next_board_state(s):

	height = len(s)
	width = len(s[0])

	next_state = []

	for i in range(0,width):
		next_state.append([next_cell_state((i,j),s) for j in range(0,height)])

	return next_state
	
def next_cell_state(coords,state):

	height = len(state)
	width = len(state[0])
	x = coords[0]
	y = coords[1]

	n_live_cells = 0

	for x1 in range(x-1,(x+1)+1):

		if x1 < 0 or x1 >= width:continue

		for y1 in range(y-1,(y+1)+1):

			if y1 < 0 or y1 >= width: continue

			if x1 == x and y1 == y: continue

			if state[x1][y1] == ALIVE:
				n_live_cells += 1

	if state[x][y] == ALIVE:

		if n_live_cells <= 1:
			return	DEAD

		if n_live_cells <= 3:
			return ALIVE

		else:
			return DEAD

	else:
		if n_live_cells == 3:
			return ALIVE
		else:
			return DEAD


def load_board_state(l):

	a = []

	with open(f'{l}') as f:
		read_data = list(f)

		for line in read_data:

			a.append([int(j) for j in line if j != '\n']) #make state and strip of the new character at the end of each line of the file

	return a

def main(s):

	while True:

		render(s,c=random.randrange(91,98))
		s = next_board_state(s)
		os.system('cls' if os.name == 'nt' else 'clear')
		#time.sleep(.03)


if __name__ == '__main__':

	b = random_state(40,40)
	main(b)

