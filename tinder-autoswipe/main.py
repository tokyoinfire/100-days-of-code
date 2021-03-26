from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

URL = "https://tinder.com/"
FB_LOGIN = ""
FB_PASSWORD = ""

chrome_driver_path = r"C:\Users\1\Desktop\chrome_driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path = chrome_driver_path)

driver.get(URL)

time.sleep(5)

enter_button = driver.find_element_by_xpath(
    '//*[@id="t--771258051"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button'
)
enter_button.click()

time.sleep(5)

another_button = driver.find_element_by_xpath(
    '//*[@id="t-1483503441"]/div/div/div[1]/div/div[3]/span/button'
)
another_button.click()

time.sleep(5)

facebook_login = driver.find_element_by_xpath(
    '//*[@id="t-1483503441"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]'
)
facebook_login.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

time.sleep(5)

login = driver.find_element_by_name("email")
login.send_keys(FB_LOGIN)

password = driver.find_element_by_name("pass")
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

allow_button = driver.find_element_by_xpath(
    '//*[@id="t-1483503441"]/div/div/div/div/div[3]/button[1]'
)
allow_button.click()

no_button = driver.find_element_by_xpath(
    '//*[@id="t-1483503441"]/div/div/div/div/div[3]/button[2]'
)
no_button.click()

for n in range(100):

    time.sleep(1)

    try:
        print("called")
        like_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button'
        )
        like_button.click()

    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        except NoSuchElementException:
            time.sleep(2)

driver.quit()
