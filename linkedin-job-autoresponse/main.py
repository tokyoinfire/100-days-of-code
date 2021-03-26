from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = r"C:\Users\1\Desktop\chrome_driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path = chrome_driver_path)
URL = "https://www.linkedin.com/jobs/search/?f_AL=true&geoId=107245803&keywords=Python-%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&location=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%20%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%20%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F"
LOGIN = ""
PASSWORD = ""
PHONE = ""

driver.get(URL)
sign_in_button = driver.find_element_by_link_text("Войти")
sign_in_button.click()

time.sleep(10)

login = driver.find_element_by_id("username")
login.send_keys(LOGIN)

password = driver.find_element_by_id("password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

time.sleep(30)

all_listings = driver.find_elements_by_css_selector(".jobs-search-results__list")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    try:
        apply_button = driver.find_element_by_css_selector(".jobs-apply button")
        apply_button.click()
        time.sleep(5)

        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element_by_css_selector("footer button")

        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
