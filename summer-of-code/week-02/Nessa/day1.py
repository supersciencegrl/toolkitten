import unittest

from moo import moo

# moo(3)

# ### READING AND WRITING FILES ###

filename = "bot-library.csv"
file = open(filename, "r")

# for line in file:
	# print(line)
	
raw = file.read()

# print 1st-65th characters
# print(raw[:65])

print("")

# print 66th-100th characters
# print(raw[65:100])

print("Total characters in " + filename + ": " + str(len(raw)))
print("")

# ### CHARACTER CALCULATOR ###

# Calculate how many times each letter of the alphabet appears in bot-library.csv

from string import ascii_lowercase

print("Frequency distribution of characters in bot-library.csv: ")
count = 0
for a in ascii_lowercase:
	for r in raw:
		if r == a:
			count = count + 1
			
	row = [a, count]
	print("{:<3} {:<8}".format(*row))
	count = 0

# ### RECURSIVE QUESTION ###
	
def ask_recursively(question):
	print(question)
	reply = input("> ").lower()
	if reply == "yes":
		return True
	elif reply == "no":
		return False
	else:
		print("Please answer 'yes' or 'no'!")
		ask_recursively(question)
		
ask_recursively("Do you like cats?")