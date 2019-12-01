import random

bars = ["Shoolbred's",
        "The Wren",
        "The Scratcher",
        "ACME",
        "Blind Barber"]

people = ["Mattan",
          "Chris",
          "that person you forgot to text back",
          "Kanye West",
        #Challenge : 1 Change Name to : Samuel L. Jackson
          "Samuel L. Jackson",
        #Challenge : 2 Add a Friend to the List
          "Humza"
          ]

random_bar = random.choice(bars)
random_person_one = random.choice(people)
# Challenge : 3 Selecting 2 Random People
random_person2 = random.choice(people)
print(f"How about you go to {random_bar} with {random_person_one} and {random_person2}")
