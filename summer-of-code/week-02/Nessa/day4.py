# import cool_int

# ### RENAMING MODULES ###

import cool_int as ci

# Now you only have to type 'ci' each time you need cool_int

ci.to_eng(5)
ci.to_eng(41)

toy = ci.awesome_cat["fav_toy"]

print(toy)

# Avoid typing cool_int OR ci: 

from cool_int import awesome_cat

colour = awesome_cat["colour"]

print(colour)

# Import details about the computer you're running this on
import platform

p = platform.system()
print(p)

# Import the OS - allows you to create files, navigate directories, etc
import os

# List directory of names belonging to a module
# "Peek inside the module"
d = dir(platform)
# print(d)

p = platform.python_compiler()
print(p)