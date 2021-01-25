# number = input("Input your number:")
#
# print(int(number[0]) + int(number[1]))

# height = float(input("enter your height:\n"))
# weight = int(input("enter your weight:\n"))
#
# print(int(weight / (height ** 2)))

# age = int(input('What is your age?\n'))
#
# years_remaining = 90 - age
# days_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# months_remaining = years_remaining * 12
#
# message = f"You have {days_remaining} days, {months_remaining} months, {weeks_remaining} weeks, {years_remaining} years"
#
# print(message)
# print(int((age * 365) // 7))

print("welcome to the tip calculator")

bill = int(input("What was the total bill? $ "))
percantage = int(input("What percentage tip would you like to give? 10, 12, 15 or 20? "))
people = int(input("How many people to split the bill? "))

bill = int((bill * (percantage/100)) + bill)
total = round(bill / people, 2)
print(f"Each person should pay: ${total}")