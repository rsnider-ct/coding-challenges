# Example code from the lecture section. Feel free to play around with this!
import random

# The given list of words
list = ["test", "list", "of", "random", "words"]

# Generate a random number
randomInteger = random.randint(0, 4)

# And finally, print it out
print list[randomInteger]


# And, if you feel like 2 lines is too much, you could also do it like this.
# Just uncomment and give it a whirl!
#print list[random.randint(0,4)]