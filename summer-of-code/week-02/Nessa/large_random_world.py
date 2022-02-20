# ### LARGE RANDOM WORLD ###

import random

unit = "...xx"
world = []

n = int(input("What is the dimension of your world? "))

print("Welcome to your new world!")

y = 0
while y < n:
	line = []
	x = 0
	while x < n:
		line.append(random.choice(unit))
		x = x + 1
	world.append(line)
	y = y + 1

for w in world:
	print("[%s]" % " ".join(map(str, w)))

# ### CONTINENT COUNTER ###

# Once you've counted land, turn to 0 so don't duplicate counting
def continent_counter(world, x, y):
	if world[y][x] != "x":
		return 0
	world[y][x] = "o"
	size = 1
		
	# 8 tiles around (x,y)
	# Recursive: tiles around neighbours also counted
	size = size + continent_counter(world, x-1, y-1)
	size = size + continent_counter(world, x, y-1)
	size = size + continent_counter(world, x+1, y-1)
	size = size + continent_counter(world, x-1, y)
	size = size + continent_counter(world, x+1, y)
	size = size + continent_counter(world, x-1, y+1)
	size = size + continent_counter(world, x, y+1)
	size = size + continent_counter(world, x+1, y+1)
	return size

print("")
print("Middle continent size: " + str(continent_counter(world, int((n+1)/2), int((n+1)/2))))

# Bug: when the central continent borders the edge, the recursion tries to move outside the grid. I don't know how to fix this yet... 