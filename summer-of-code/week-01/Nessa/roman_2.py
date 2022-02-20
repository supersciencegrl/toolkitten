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