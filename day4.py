import random

#
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)
# random_number = random.randint(0,1)
#
# if random_number == 1:
#     print("Heads")
# else:
#     print("Tails")
#
# namesAsCSV = input("Give me everybody's names: ")
# names = namesAsCSV.split(", ")

# num_items = len(names)
# random_choise = random.randint(0, num_items - 1)
# person_who_will_pay = names[random_choise]
# person_who_will_pay = random.choice(names)
#
# print(f"{person_who_will_pay} is going to buy meal today")


# row1 = ["O", "O", "O"]
# row2 = ["O", "O", "O"]
# row3 = ["O", "O", "O"]
# map = [row1, row2, row3]
#
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put your treasure?\n")
#
# horizontal = int(position[0]) - 1
# vertical = int(position[1]) - 1
#
# map[vertical][horizontal] = "X"
#
# print(f"{row1}\n{row2}\n{row3}")


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
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw")
