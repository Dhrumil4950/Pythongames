import turtle
import time
import random
WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'pink', 'green','orange', 'black', 'purple','brown','cyan','yellow','blue'] # Selects some colors regarding user input for e.g.: user input 3 Racers: only first 3 colors of turtle race.

def get_num_racers(): #Defenition asks user to give input from range 2 to 10 to race...
	racers = 0
	while True:
		racers = input('Enter the number of racers (2 - 10): ')
		if racers.isdigit():
			racers = int(racers)
		else:
			print('Input is not valid...!')
			continue

		if 2 <= racers <= 10:
			return racers
		else:
			print('Number is not in range!')
def race(colors):   # choose colors of the number of racers
	turtles = create_turtles(colors)

	while True: 
		for racer in turtles:
			distance = random.randrange(1, 20)
			racer.forward(distance)


			x, y = racer.pos()
			if y >= HEIGHT//2 - 10:
				return colors[turtles.index(racer)]

def create_turtles(colors):  # alline turtles in one line of choosen colors. put them on START Line of Race track 
	turtles = []
	spacingx = WIDTH // (len(colors) + 1)
	for i, color in enumerate(colors):
		racer = turtle.Turtle()
		racer.color(color)
		racer.shape('turtle')
		racer.left(90)
		racer.penup()
		racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
		racer.pendown()
		turtles.append(racer)

	return turtles


def init_turtle():  # setting screen width, height and title using this definition
	screen = turtle.Screen()
	screen.setup(WIDTH, HEIGHT)
	screen.title('Turtles are racing')

racers = get_num_racers()

init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)
print("The winner is turtle with color:", winner)  # Will display the winner with the color specified of winner
time.sleep(5)


