# import math
#
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
#
# coverage = 5
#
#
# def paint_calc(height, width, cover):
#     needed = math.ceil((height * width) / coverage)
#     print(f"You'll need to buy {needed} cans of paint")
#
#
# paint_calc(height=test_h, width=test_w, cover=coverage)


# def prime_checker(number):
#     check = True
#     for m in range(2, number - 1):
#         if number % m == 0:
#             check = False
#     if check:
#         print("It's a primal number")
#     else:
#         print("It's not a primal number")
#
#
# n = int(input("Check this number: "))
# prime_checker(number=n)

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode" :
        shift_amount *= -1
    for char in start_text :

        if char in alphabet :
            position = alphabet.index ( char )
            new_position = position + shift_amount
            end_text += alphabet [ new_position ]
        else :
            end_text += char
    print ( f"Here's the {cipher_direction}d result: {end_text}" )


should_end = False
while not should_end:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
