from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

PASSWORD = ''
LOGIN = ''
CHROME_DRIVER_PATH = r"C:\Users\1\Desktop\chrome_driver\chromedriver.exe"
SIMILAR_ACCAOUNT = 'kimkardashian'


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path = CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get('https://www.instagram.com/')

        time.sleep(10)

        login = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[1]/div/label/input'
        )
        login.send_keys(LOGIN)

        password = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[2]/div/label/input'
        )
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)

        time.sleep(10)

        not_now_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/div/div/button'
        )
        not_now_button.click()

        time.sleep(10)

        notifications_off_button = self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div[3]/button[2]'
        )
        notifications_off_button.click()

        

    def find_followers(self):
        self.driver.get('https://www.instagram.com/kimkardashian/')

        time.sleep(10)

        followers_link = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'
        )
        followers_link.click()

        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector('li button')

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath(
                    '/html/body/div[5]/div/div/div/div[3]/button[2]'
                )
                cancel_button.click()


instafollower = InstaFollower()

instafollower.login()
instafollower.find_followers()
instafollower.follow()

