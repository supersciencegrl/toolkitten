# ### CALC ###

print("")
print("### CALC ###")
print("")

print("Hours in a year:")
print(24*365)

print("Minutes in a decade:")
print(60*24*365*10)

print("My age in seconds:")
print((365*27+6+2+31+30+31+30+16)*24*1440)
# Correct to the nearest day at the time of writing! 

print("Andreea's age:")
print(48618000/(365*24*1440))
print("?!")

# ### FULL NAME ###

print("")
print("### WHAT'S YOUR NAME ###")
print("")

import random

first_name = input("What is your first name? ")
middle_name = input("What is your middle name? ")
last_name = input("What is your surname? ")

greeting = ["Hello, ", "Hi, ", "Bonjour, ", "salve, "]

print(random.choice(greeting) + first_name + " " + middle_name + " " + last_name + "!")

# ### BETTER FAVOURITE NUMBER ###

print("")
print("### BETTER FAVOURITE NUMBER ###")
print("")

fave = str(int(float(input("What is your favourite number? ")) + 1))

print("Oh come on, how about " + fave + "... that's bigger and better!")

# ### TEN GREEN BOTTLES ###

print("")
print("### TEN GREEN BOTTLES ###")
print("")
x = 10
while x > 1:
	y = str(x)
	print((y + " green bottles, standing on a wall, ") * 2)
	print("And if one green bottle should accidentally fall")
	x = x - 1
	y = str(x)
	if x > 1:
		print("There'll be " + y + " green bottles, standing on the wall.")
		print("")
	else:
		print("There'll be " + y + " green bottle, standing on the wall.")
		print("")
	
while x == 1:
	y = str(x)
	print((y + " green bottle, standing on a wall, ") * 2)
	print("And if one green bottle should accidentally fall")
	print("There'll be no green bottles, standing on the wall.")
	x = x - 1
	
print("")
print("Fin.")

# ### DEAF GRANDMA ###

import random

year = random.randint(1938, 1950)

text = ""
utext = " "
while utext != text:
	text = input("WHAT'S UP WITH YOU?! ")
	utext = text.upper()
	if utext != text:
		print("HUH?! SPEAK UP, GIRL! ")
	
print("NO, NOT SINCE " + str(year) + "!")

# ### LEAP YEARS ###

print("")
print("### LEAP YEARS ###")
print("")

i_year = int(input("First year: "))
f_year = int(input("Last year: "))

c_year = i_year
while c_year != f_year + 1:
	if c_year % 4 == 0:
		if c_year % 100 != 0:
			print(c_year)
		elif c_year % 400 == 0:
			print(c_year)
	c_year = c_year + 1
	if c_year == f_year + 1:
		break

# ### ALPHABETIZE ###

text = " "
words = []
while text != "":
	text = input("Add your word here: ")
	if text != "":
		words.append(text)
	
print(sorted(words))
		
# ### MOO ###

print("")
print("### MOO ###")
print("")

n = int(input("How many cows do you have? "))

def moo(n):
	print("moo " * n)
	
moo(n)
	
# ### EARLY ROMAN NUMERALS ###

print("")
print("### EARLY ROMAN NUMERALS ###")
print("")

n = int(input("Input a number. "))

m = n // 1000
n = n - m * 1000

d = n // 500
n = n - d * 500

c = n // 100
n = n - c * 100

l = n // 50
n = n - l * 50

x = n // 10
n = n - x * 10

v = n // 5
n = n - v * 5

print("M" * m + "D" * d + "C" * c + "L" * l + "X" * x + "V" * v + "I" * n)

# ### LATE ROMAN NUMERALS ###

print("")
print("### LATE ROMAN NUMERALS ###")
print("")

n = int(input("Input a number. "))

m = n // 1000
n = n - m * 1000

n1 = n
d = n // 500
n = n - d * 500
c = n // 100
n = n - c * 100

if n1 // 100 == 9:
	c1 = "CM"
else:
	c1 = "D" * d + "C" * c

n1 = n1
l = n // 50
n = n - l * 50
x = n // 10
n = n - x * 10

if n1 // 10 == 9:
	x1 = "XC"
else:
	x1 = "L" * l + "X" * x

n1 = n
v = n // 5
n = n - v * 5

if n1 == 9:
	i1 = "IX"
else:
	i1 = "V" * v + "I" * n

print("M" * m + c1 + x1 + i1)

