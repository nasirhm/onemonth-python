the_count = [1,2,3,4,5]

the_stock = ["AAPL","GOOG","TSLA"]

listinlist = ["Lst",["Oopos","List Inside a List"]]

for number in the_count:
    print("this is count", number)

#Stock Ticker : Same as Above
for stock in the_stock:
    print("Stock Ticker", stock)

for i in listinlist:
    print("List",i)

# Making (Initializing) an Empty List
people = []
people.append("Mattan")
people.append("Sarah")
people.append("Chris")
print(people)
people.remove("Sarah")
print(people)

for person in people:
    print("Person is:", person)

animals = ['bear','tiger','wolves']
first_animal = animals[0]
print(first_animal)
print("There are this many animals:", len(animals))
print("This is a ", type(animals))

another_list = listinlist[-1]
print(another_list)
print(type(another_list))