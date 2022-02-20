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
	
count = 0
for w in world:
	for w1 in w:
		if w1 == "x":
			count = count + 1
	
print("")
print("Count: " + str(count))

from string import ascii_uppercase

first_continent_size = 0
for w in world:
	y_coord = int(world.index(w))
	letter = ascii_uppercase[y_coord]
	x_coord = w.index("x") + 1
	number = str(x_coord)
	print(x_coord)
	print(y_coord)
	print("First land coordinates: " + letter + number)
	print(w[y_coord])
	break