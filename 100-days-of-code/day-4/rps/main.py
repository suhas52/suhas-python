import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)

com_choice = random.randint(0,2)
print("The computer chose:")
if com_choice == 0:
    print(rock)
elif com_choice == 1:
    print(paper)
elif com_choice == 2:
    print(scissors)

if choice == com_choice:
    print("That's a draw!")

if choice == 0 and com_choice == 1:
    print("You lose!")

if choice == 0 and com_choice == 2:
    print("You win!")

if choice == 1 and com_choice == 0:
    print("You win!")

if choice == 1 and com_choice == 2:
    print("You lose!")

if choice == 2 and com_choice == 0:
    print("You lose!")

if choice == 2 and com_choice == 1:
    print("You win!")
