def greet(name):
	return f"Hello {name}!"

def concatenate(word_one,word_two):
	return word_one + word_two

def age_in_dog_years(age):
	result = age * 7
# If no Return then None and Only one return : Return more with List and Dictionary
	return result

print(greet('Mattan'))
print(greet('Chris'))

print(concatenate('Nasir', 'Hussain'))

print(age_in_dog_years(14))

print(concatenate(word_two='Nasir',word_one='Hussain'))

name = "Mattan"

def print_different_name():
	# Scope for inside function
	name = "Chris"
	print(name)

print(name)
print_different_name()
print(name)