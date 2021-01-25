# number = int(input("What is your number? "))
#
# if number % 2 == 0:
#     print("even")
# else:
#     print("odd")

# height = float(input("enter your height:\n"))
# weight = float(input("enter your weight:\n"))
#
# bmi = round(weight / (height ** 2))
#
# if bmi < 18.5:
#     print("You're underweight")
# elif bmi < 25:
#     print("You have normal weight")
# elif bmi < 30:
#     print("You're overweight")
# elif bmi < 35:
#     print("You're obese")
# else:
#     print("You're overweight")


# year = int(input("Which year do you want to check? "))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("It is a leap year.")
#         else:
#             print("It is not a leap year.")
#     else:
#         print("It is a leap year.")
# else:
#     print("It is not a leap year.")

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# bill = 0
#
# if size == "S":
#     bill = 15
# elif size == "M":
#     bill = 20
# elif size == "L":
#     bill = 20
#
# if (add_pepperoni == "Y") and (size == "S"):
#     bill+= 2
# elif (add_pepperoni == "Y") and ((size == "M") or (size == "M")):
#     bill += 3
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your final bill is :${bill}")

# print("Welcome to the love calculator!")
# name1 = input("What is your name? ")
# name2 = input("What is their name? ")
#
# name1 = name1.lower()
# name2 = name2.lower()
# comb_name = name1 + name2
#
# true = comb_name.count("t") + comb_name.count("r") + comb_name.count("u") + comb_name.count("e")
#
# love = comb_name.count("l") + comb_name.count("o") + comb_name.count("v") + comb_name.count("e")
#
# love_score = int(str(true) + str(love))
#
# if (love_score < 10) or (love_score > 90):
#     print("Not good idea")
# elif (love_score >= 40) or (love_score <= 50):
#     print("You're alright together")
# else:
#     print(" ehhhhhh....")
#
#
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Tresure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".\n').lower()

if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You got attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")