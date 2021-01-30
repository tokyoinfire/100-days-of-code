# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
#
# student_grades = {}
#
# for key in student_scores:
#     if student_scores[key] <= 70:
#         student_grades[key] = "Fail"
#     elif student_scores[key] <= 80:
#         student_grades[key] = "Acceptable"
#     elif student_scores[key] <= 90:
#         student_grades[key] = "Exceeds Expectations"
#     elif student_scores[key] <= 100:
#         student_grades[key] = "Outstanding"
#
# print(student_grades)


# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Lille", "Dijon"]
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Hamburg", "Stuttgart"]
#     }
# ]
#
#
# def add_new_country(country, visits, cities):
#     new_country = {"country": country, "visits": visits, "cities": cities}
#     travel_log.append(new_country)
#
#
# add_new_country(country = "Russia", visits = 2, cities = ["Moscow", "Saint Petersburg"])
# print(travel_log)

from os import system
import operator

dictionary = {}
n = True


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while n:
    print("Welcome to the blind auction!")
    name = input("What is your name? ")
    price = int(input("What is your price? $"))
    check = input("Are there any bidders left?")
    dictionary[name] = price
    if check == "yes":
        clear = lambda: system('cls')
        clear()
    elif check == "no":
        clear = lambda: system('cls')
        clear()
        n = False
        find_highest_bidder(dictionary)

# winner = max(dictionary.items(), key = operator.itemgetter(1))[0]
# print(f"{winner} won with bid {dictionary[winner]}")
