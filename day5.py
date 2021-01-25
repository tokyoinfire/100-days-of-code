import random

# student_heights = input("Input a list of students heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
#
# total_sum = 0
# average_height = 0
# counter = 0
#
# for student in student_heights:
#     total_sum += student
#     counter += 1
#
# average_height = round(total_sum / counter)
# print(average_height)


# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
#
# highest_score = 0
# for student_score in student_scores:
#     if student_score > highest_score:
#         highest_score = student_score
#
# print(f"The highest score is: {highest_score}")

# total = 0
# for number in range(2, 101, 2):
#     total += number
#
# print(total)


# for number in range(1, 101):
#     output = ""
#
#     if number % 3 == 0:
#         output += "Fizz"
#
#     if number % 5 == 0:
#         output += "Buzz"
#
#     if output == "":
#         output = str(number)
#
#     print(output)
#


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []
password_string = ""

for letter in range(0, nr_letters):
    password_list += random.choice(letters)

for number in range(0, nr_numbers):
    password_list += random.choice(numbers)

for symbol in range(0, nr_symbols):
    password_list += random.choice(symbols)

random.shuffle(password_list)

for item in password:
    password_string += item

print(f"Your password is {password_string}")
