### CHR ###

# alt codes
# print(chr(176))

# print(chr(252))

### ALPHABET METHOD ONE ###

# alphabet_range = [i for i in range(65, 91)]
# range2 = [i for i in range(97, 123)]

# for r in range2:
	# alphabet_range.append(r)

# print(alphabet_range)
# for i in alphabet_range:
	# print("{:>3} {:<8} {:<8}".format(i, " stands for ", chr(i)))
	
### ALPHABET METHOD TWO ###
	
# for i in range(65,123):
	# if 90 < i < 97:
		# pass
	# else:
		# print("{:>3} {:<8} {:<8}".format(i, " stands for ", chr(i)))
		
### SECRET CODE ###

# from string import ascii_uppercase
# from string import ascii_lowercase

# plaintext = ascii_uppercase + ascii_lowercase + " "
# alphabet_range.append(32)
# cipher = ""
	
# text = input("What do you want to encode? ")

# for t in text:
	# cipher_index = plaintext.index(t)
	# cipher_t = str(alphabet_range[cipher_index])
	# cipher = cipher + cipher_t + " "

# print(cipher)

### DECRYPTION ###

# plaintext_d = ""
# cipher_d = input("What do you want to decode? ")
# cipher_list = [int(d) for d in cipher_d.split()]

# for c in cipher_list:
	# print(c)
	# plaintext_index = alphabet_range.index(c)
	# print(plaintext_index)
	# plaintext_c = str(plaintext[plaintext_index])
	# print(plaintext_c)
	# plaintext_d = plaintext_d + plaintext_c
	# print("")
	
# print(plaintext_d)

# ### RANDOM WORLD ###

import random

unit = "...xx"
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
print("Middle continent size: " + str(continent_counter(world, 5, 5)))
print("")

# Bug: when the central continent borders the edge, the recursion tries to move outside the grid. I don't know how to fix this yet... 
# Look into trace function to stop this? 

# ### BACKWARDS WORLD ### #

world_rev = []
line_rev = []
temp = []

for y in range(11):
	for x in range(11):
		if world[y][x] == "o":
			world[y][x] = "x"

for i in range(10, -1, -1):
	line = world[i]
	for j in range(10, -1, -1):
		line_rev.append(line[j])
	world_rev.append(line_rev)
	line_rev = []
		
print("Let's turn your world upside down")
print("(And back to front):")
print("")
		
for w in world_rev:
	print("[%s]" % " ".join(map(str, w)))
