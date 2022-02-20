# ### ALPHABETIZE ###

text = " "
words = []
while text != "":
	text = input("Add your word here: ")
	if text != "":
		words.append(text)
	
print(sorted(words))