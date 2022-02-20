# ### TEN GREEN BOTTLES ###

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