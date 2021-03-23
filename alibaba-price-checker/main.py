import requests
from bs4 import BeautifulSoup
import smtplib

my_email = ""
password = ""

response = requests.get("https://www.alibaba.com/product-detail/Professional-Lenovo-Gaming-Laptop-Legion-Y7000P_1600051585477.html?spm=a2700.galleryofferlist.normal_offer.d_image.5cdd349duYPRXX").text

soup = BeautifulSoup(response, "html.parser")

price = soup.find_all(name = "div", class_="sku-price__sku-price-item")

price_list = [float(price.getText().replace("$", "").replace(",", "")) for price in price]

for price in price_list:
    if price < 1500:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user = my_email, password = password)
            connection.sendmail(
                from_addr = my_email,
                to_addrs = "sveklenko15@gmail.com",
                msg = f"Subject:Price for your laptop is less than $1300!\n\nNow it is ${price}")
            connection.close()
