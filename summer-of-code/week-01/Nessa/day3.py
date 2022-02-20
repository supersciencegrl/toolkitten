i = 0
while i < 12:
	print(i)
	i = i + 1
	if i == 4:
		break
		
# j += 1 is the same as j = j + 1

text=""
# while text != "bye":
	# text = input("What do you want to say (bye to exit)? ")
	# print("You're saying " + text + "?")
	
# print("Bye for now!")

for x in range(1, 20, 2):
	print(x)

cats = ["Elliott", "Faraday", "Susie", "Pounce"]

for c in cats:
	if len(c) > 6:
		print(c + " is a very good cat!")
	elif len(c) == 6:
		print(c + " really is a great cat!")
	else:
		print(c + ": what a great cat!")
		
cats.append("Poppy")

# for c in cats:
	# print(c)
	
cat_user = [c+"_cat" for c in cats]
cat_usernames = []

for c in cat_user:
	c = c.lower()
	cat_usernames.append(c)

print("Ordered cat usernames: ")
print(sorted(cat_usernames))