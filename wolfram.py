import random
import subprocess

def get_rule(n): #return rule as binary from rule number

	def make_8(s): #makes string 8 long by adding zeroes to the string
		return f'0'*(8-len(str(s)))+str(s)

	binary_list = [int(f'{i:b}') for i in range(0,255)] #i:b returns a binary representation of the deicmals b/w 0 and 255 without the 0b encoding
	b = [make_8(i) for i in binary_list] #uses the padding function
	rule_list = list(enumerate(b,0)) #get the rules indexed

	for i in rule_list:
		if i[0] == n:
			return i[1]

def apply_rule(c,r):

	def get_neighbors(c):
		a = []
		s = f'00{c}00'

		for j in range(len(c)+2):
			a.append(f'{s[j]}'+f'{s[j+1]}'+f'{s[j+2]}')

		return a

	init = ['111','110','101','100','011','010','001','000'] #determines the order of rule application, never changes
	s = ''

	for i in get_neighbors(c):
		if i in init:
			s += f'{get_rule(r)[init.index(i)]}'
	
	return s

def render(s):
	n = random.randint(91,98)
	s = s.replace('0',' ').replace('1', u"\u2588").center(200)
	subprocess.call('', shell=True) #there is a bug that requries this to display ANSII color characters
	print(f'\033[{n}m{s}\033[0m')

def run(c,r):
	i = 0
	cell = c
	while i<100:
		render(cell)
		cell=apply_rule(cell,r)
		i += 1

def run_all():
	for i in range(0,255):
		run('1',i)


if __name__ == '__main__':

	#rule = int(input("rule: "))

	for i in range(255):
		run('1',random.randrange(255))






