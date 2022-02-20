# ### LEAP YEARS ###

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