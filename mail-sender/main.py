import smtplib
import random
import datetime as dt

my_email = "smth@gmail.com"
password = "1234567890qwerty"


now = dt.datetime.now()

if now.weekday() == 0:

    with open("quotes.txt", encoding="utf8") as file:
        quotes = file.readlines()
        msg_quote = random.choice(quotes).encode('ascii', 'ignore').decode('ascii')

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email, password = password)
        connection.sendmail(
            from_addr = my_email,
            to_addrs = "sveklenko15@gmail.com",
            msg = f"Subject:Your Weekly Motivation\n\n{msg_quote}"
        )
        connection.close()

print(msg_quote)
