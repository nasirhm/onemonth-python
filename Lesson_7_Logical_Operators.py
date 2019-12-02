# and, or , not, ==, !=, >, and <
answer = input("Do you Want to Hear a Joke")
#Lists.
affirmative_responses = ["yes","y"]
negative_responses = ["no","n"]

#Or Reason for comparing again it would always return true due to the nature of Strings

#.lower for Lowercasing the Input
if answer.lower() in affirmative_responses:
    print("No Joke, Go Home")
elif "n" in answer.lower():
    print("Fine")
else:
    print("I Don't Understand")


#2 if y in answer.lower()