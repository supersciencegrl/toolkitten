# ### DICTIONARY ###

my_dict = {
	"a": 35000,
	"b": 8000,
	"z": 450
}

# A dictionary is unordered and does not contain repeat strings

# Access dictionary
print("A in my_dict: " + str(my_dict["a"]))
print("Dictionary length: " + str(len(my_dict)))
# Dictionary length = number of keys

# Add to dictionary
my_dict["q"] = "something"

# Modify dictionary
my_dict["a"] = 500

# Delete key from dictionary
del(my_dict["a"])

# Or delete whole dictionary
# del(my_dict)

# ### MODIFY q TO "FARADAY" IN my_dict ###
print("")
print("Original dictionary: ")
print(my_dict)

my_dict["Faraday"] = my_dict["q"]
del(my_dict["q"])

print("")
print("New dictionary: ")
print(my_dict)

# ### DICTIONARY CONSTRUCTOR ###
# Creating a dictionary is called "instantiating"... 

Faraday = dict(name = "Faraday", fav_toy = "fishing rod", fav_food = "Purina")
Elliott = dict(name = "Elliott", fav_toy = "hexbug", fav_food = "Purina")

print(Faraday)

# ### FREQUENCY DISTRIBUTION DICTIONARY ###

filename = "bot-library.csv"
file = open(filename, "r")
	
raw = file.read()

bot_dict = {}

from string import ascii_lowercase

count = 0
for a in ascii_lowercase:
	for r in raw:
		if r == a:
			count = count + 1
			
	bot_dict[a] = count
	count = 0

print("")
print("Frequency distribution of letters in bot-library.csv as a dictionary: ")
print(bot_dict)

# ### MY DICTIONARY ###

Nessa = dict(name = "Nessa Carson", obsession = "chemistry", best_friend = "QX96 dosing robot")

print(Nessa)

# ### MAPPING WITH CITIES AND REGIONS IN YOUR COUNTRY ###
# Alt.: mapping element symbols to atomic numbers

class Element():
	def __init__(self, name, symbol, Z):
		self.name = name
		self.symbol = symbol
		self.Z = Z
	
# Instantiate
e1 = Element("hydrogen", "H", 1)
e2 = Element("helium", "He", 2)
e3 = Element("lithium", "Li", 3)
e4 = Element("beryllium", "Be", 4)
e5 = Element("boron", "B", 5)


# ### CLASSES ###

class Kitty():
	def __init__(self, name, colour, gender):
		self.name = name
		self.colour = colour
		self.gender = gender
		
# self is just a convention. name and name are different but this is also convention to make them identical
	
# Instantiate
k1 = Kitty("Elliott", "black & white", "boy")
k2 = Kitty("Faraday", "ginger", "boy")
k3 = Kitty("Susie", "black & white", "girl")
k4 = Kitty("Scrappy", "ginger", "boy")
k5 = Kitty("Pounce", "black & white", "boy")

# print(k3.name)
# print(k4.gender)

# ### PRINT ALL DETAILS ###

def print_all(self):
	print(self.name + ", " + self.colour + ", " + self.gender)
	
print_all(k1)

# ### MODIFY CATS ###

k2.colour = "ginger & white"

print_all(k2)

# Delete properties
# del k1.gender
# Likely to create errors as the attribute will no longer exist but functions may try to access it

# ### 1MWTT CLASS ###

class Student():
	def __init__(self, first_name, last_name, email, country, github_id, discord_id, vol_status, gold_status, vip_status, coding_level, dream):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.country = country
		self.github_id = github_id
		self.discord_id = discord_id
		self.vol_status = vol_status
		self.gold_status = gold_status
		self.vip_status = vip_status
		self.coding_level = coding_level
		self.dream = dream
		
