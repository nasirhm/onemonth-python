# Lists
# states = ['NY', 'PY', 'CA']
# states = ['New York', 'Pennsylvania', 'Califonia']

# Dictionary Key:Value : Keys are necessary to be Strings, They are fast if even its long
states = {'NY': 'New York', 'PA': 'Pennsylvania', 'CA': 'Califonia'}

print(states['NY'])
print(type(states))
# None Error, Default Error
print(states.get('FL', 'Not Found'))
print(states.get('NY', 'Not Found'))

print(states.keys())
print(states.values())

# Adding in List
states['FL'] = 'Florida'
print(states)

# Dictionaries & Lists inheritance

animal_sounds = {
	"Cat": ["Meow", "Purr"],
	"Dog": ["Woof", "Bark"],
	"Fox": []
}

nasir = {'name': 'Nasir', 'height':70,'Shoe Size': 10.5, 'hair':'Brown','eyes': 'Brown'}
chris = {'name': 'Chris', 'height':70,'Shoe Size': 10.5, 'hair':'Brown','eyes': 'Brown'}
sarah = {'name': 'Sarah', 'height':70,'Shoe Size': 10.5, 'hair':'Brown','eyes': 'Brown'}

people = [nasir, chris, sarah]

print(people)

# Printing Height
for person in people:
	print(person.get('height'))