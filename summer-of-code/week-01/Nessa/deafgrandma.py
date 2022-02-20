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