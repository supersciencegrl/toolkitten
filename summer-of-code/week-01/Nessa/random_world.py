import random

unit = "oooxx"
world = []

print("Welcome to your new world!")

y = 0
while y < 11:
	line = []
	x = 0
	while x < 11:
		line.append(random.choice(unit))
		x = x + 1
	world.append(line)
	y = y + 1
	
for w in world:
	print("[%s]" % " ".join(map(str, w)))