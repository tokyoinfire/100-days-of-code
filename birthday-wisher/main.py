##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import smtplib
import random


email = "smth@gmail.com"
password = "1234567890qwerty"

birthdays_csv = pandas.read_csv("birthdays.csv")
today = (dt.datetime.now().month, dt.datetime.now().day)

birthday_dict = {(row.month, row.day): row for (index, row) in birthdays_csv.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(email, password)
            connection.sendmail(
                from_addr = email,
                to_addrs = birthday_person["email"],
                msg = f"Subject:Happy Birthday!\n\n{content}"
            )






