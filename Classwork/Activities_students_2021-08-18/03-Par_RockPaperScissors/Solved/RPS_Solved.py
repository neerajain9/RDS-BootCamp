# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if user_choice == 'r' and computer_choice == 'r':
    print("You chose rock, the computer chose rock.")
    print("A smashing tie!")
elif user_choice == 'r' and computer_choice == 'p':
    print("You chose rock, the computer chose paper.")
    print("You lose! ':('")
elif user_choice == 'r' and computer_choice == 's':
    print("You chose rock, the computer chose scissors.")
    print("You Won! ':)'")
elif user_choice == 'p' and computer_choice == 'r':
    print("You chose paper, the computer chose rock.")
    print("You Won! ':)'")
elif user_choice == 'p' and computer_choice == 'p':
    print("You chose paper, the computer chose paper.")
    print("A smashing tie!")
elif user_choice == 'p' and computer_choice == 's':
    print("You chose paper, the computer chose scissors.")
    print("You lose! ':('")
elif user_choice == 's' and computer_choice == 'r':
    print("You chose paper, the computer chose rock.")
    print("You lose! ':('")
elif user_choice == 's' and computer_choice == 'p':
    print("You chose paper, the computer chose paper.")
    print("You Won! ':)'")
elif user_choice == 's' and computer_choice == 's':
    print("You chose paper, the computer chose scissors.")
    print("A smashing tie!")
else:
    print("I do not Understand that!")
    print("Make valid Choice: (r)ock, (p)aper, (s)cissors? ")
