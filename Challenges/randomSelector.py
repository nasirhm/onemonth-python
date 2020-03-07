# Acceptance Criteria :
#   - Defining a List (Array)
#   - importing random
#   - printing a random item from the List

# Solution :

# Importing random
import random

# Defining a list for my favourite films & TV shows
my_favourite_films = ["Frozen 2", "Frozen", "The Girl Next Door", "Friends"]

# Using append to add a film to the list
my_favourite_films.append("Mary Poppins Returns")

# Using insert to define the position of the item to be inserted in the list
my_favourite_films.insert(3, "To all the boys i've loved")

# Using random to select a random item from the my_favourite_films
random_film = random.choice(my_favourite_films)

# Printing random_film
print(f"How about watching: {random_film}")

# To execute it: python3 randomSelector.py
# Response: How about watching: [random item from my_favourinte_films]