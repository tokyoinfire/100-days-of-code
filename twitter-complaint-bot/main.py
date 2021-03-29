from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 100
PROMISED_UP = 100
CHROME_DRIVER_PATH = r"C:\Users\1\Desktop\chrome_driver\chromedriver.exe"
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path = CHROME_DRIVER_PATH)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]'
        )
        go_button.click()
        time.sleep(60)

        self.up = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
        ).text
        self.down = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span'
        ).text

        print(f"down: {self.down}")
        print(f"up: {self.up}")

    def tweet_at_provider(self):
        if float(self.down) < 100 or float(self.up) < 100:
            self.driver.get("https://twitter.com/")

            time.sleep(10)

            enter_button = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div'
            )
            enter_button.click()

            login = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
            )
            login.send_keys(TWITTER_EMAIL)

            password = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'
            )
            password.send_keys(TWITTER_PASSWORD)
            password.send_keys(Keys.ENTER)

            time.sleep(10)

            tweet_button = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div'
            )
            tweet_button.click()

            tweet_message = self.driver.find_element_by_xpath(
                '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div'
            )
            tweet_message.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when"
                                    f"I pay for 100down/100up?")

            commit_button = self.driver.find_element_by_xpath(
                '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[4]/div/div/div[2]/div[4]'
            )
            commit_button.click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

