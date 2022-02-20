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