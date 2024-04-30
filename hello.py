# Ask user for their name
name = input("What's your name? ").strip().title()

# List of family members
family = ['Mark', 'Inga', 'Michael', 'Melody', 'Ralph', 'Letecia']

# Check if the user's name is in the family list
if name in family:
    print(f"Hello {name} Myers!")
else:
    name2 = input("What is your full name?")
    print(f"Hello {name2}, you are now a friend of the family!")

# Ask the user the following questions
question = input("Where are you from? ")
print("Hello " + name + " from " + question)

question2 = input("How old are you? ")
print("Hello " + name + " from " + question + " who is " + question2 + " years old.")

question3 = input(" And where do you currently live? ")
print("Hello " + name + " from " + question + " who is " + question2 + " years old" + " and now lives in " + question3 + ".")

question4 = input("And what about work, what is your job? ")
print("Hello " + name + " from " + question + " who is " + question2 + " years old" + " and now lives in " + question3 + " and works as a " + question4 + ".")
