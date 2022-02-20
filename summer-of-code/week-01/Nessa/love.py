# Take only the part before decimal point
print(int(1.2))
print(float(1.2))
print(complex(1.2))

# Indices
print("cats"[0])
print("cats"[2])
print("cats"[1])

i = 3

print ("cats"[i])
print("")

name = "Nessa Carson"

for i in range (0,12):
	print(name[i])

x = len(name)

for i in range (0,x):
	print(name[i])
	
# If i modulus 2 is an integer (it's even)
for i in range (0,14):
	if i % 2 == 0:
		print(i)

for i in range (0,x):
	if i % 2 == 0:
		print(name[i])
		
# For odd values of i
for i in range (0,x):
	if i % 2 == 1:
		print(name[i])

result = ""
		
for i in range(0,x):
	if i % 2 == 0:
		result = result + name[i]
		print("result is " + result)
		
print("Final result is " + result)

print(name[-1])
print(name[-2])
print(name[-x])

pet = input("What is your lion's name? ")
pgender = input("Are they a boy or a girl? ")

# if pgender == "boy":
	# print(pet + " is a good boy.")
# elif pgender == "girl":
	# print(pet + " is a good girl.")
	
print(pet + " is a good " + pgender)

a = 57
b = input("Pick a number. ")

if a < int(b):
	print("You win!")
elif a == int(b):
	print("You found a!")
else:
	print("You lose!")
	