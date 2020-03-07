# Acceptance Criteria
#   - Defining a function `uppercase` that will take a string as an input and returns it in Uppercase
#   - Defining a function `reverse` that will take a string as an input and return the reversed sting as output
#   - Defining a function `lowercase` that will take a string as an input and returns it in Lowercase
#   - Defining 2 functions `uppercase_and_reverse` and `lowercase_and_reverse`
#   Additional Point : defining 2 more function & utilizing the functions defined above for the combined one

#Solution :

def upperCase(text):
    return text.upper()

def lowerCase(text):
    return text.lower()

def reverse(text):
    return text[::-1]

def upperCase_and_reverse(text):
    #Chaining both in one line
    return text.upper()[::-1]

def lowerCase_and_reverse(text):
    return text.lower()[::-1]

# Additional Points
def _upperCase_and_reverse_(text):
    upperCasedText = upperCase(text)
    reversedText = reverse(upperCasedText)
    return(reversedText)

def _lowerCase_and_reverse_(text):
    lowerCasedText = lowerCase(text)
    reversedText = reverse(lowerCasedText)
    return(reversedText)

# Calling the Defined Functions
print(f"Calling upperCase() {upperCase('Hello World!')}")
print(f"Calling lowerCase() {lowerCase('HELLO WORLD!')}")
print(f"Calling reverse() ", reverse("Hello World!"))
print(f"Calling uppercase_and_reverse() {upperCase_and_reverse('Hello World!')}")
print(f"Calling lowercase_and_reverse() ", lowerCase_and_reverse("Hello World!"))
print(f"Calling _uppercase_and_reverse_() {_upperCase_and_reverse_('Hello World!')}")
print(f"Calling _lowercase_and_reverse_()", _lowerCase_and_reverse_('Hello World!'))