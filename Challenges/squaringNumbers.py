# Acceptance Criteria :
#   - Defining a list of numbers from 1 to 10
#   - A loop to square each item of the list
#   - Additional Point : using thw ** sign to square
#   - Additional Point : using list(range(1,11)) instead of the array

# Solution :

# Defining a list with 10 numbers

numbers_to_be_squared = [1,2,3,4,5,6,7,8,9,10]

#Defining a `for` loop to square each item of the list

for number in numbers_to_be_squared:
    print(f"The square of the number {number} is {number*number}")
    # Additional point for ** sign
    print(f"The square of the number {number} is {number**2}")


# Additional Point : If the list [numbers] is not defined that could be replaced by list(range(1,11))

for number in list(range(1,11)):
    print(f"Thw square of {number} is {number**2}")