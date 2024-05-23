from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


PROMISED_DOWN = 1000
PROMISED_UP = 1000
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 100
        self.up = 100

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element(By.CLASS_NAME, value="start-text")
        time.sleep(3)
        go_button.click()
        time.sleep(45)

        self.down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/'
                                                             'div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]'
                                                             '/div/div[2]/span')
        self.up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]'
                                                           '/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/'
                                                           'div[2]/span')

    def tweet_at_provider(self):
        self.driver.get('https://x.com/')
        time.sleep(3)
        sign_in = self.driver.find_element(By.LINK_TEXT, value="Sign in")
        sign_in.click()
        time.sleep(3)

        email = self.driver.find_element(By.NAME, value='text')
        email.send_keys(TWITTER_EMAIL)
        next_button = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]'
                                                               '/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
        next_button.click()
        time.sleep(10)

        password = self.driver.find_element(By.NAME, value="password")
        password.send_keys(TWITTER_PASSWORD)
        log_in = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]'
                                                          '/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
        log_in.click()
        time.sleep(3)

        post_description = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/'
                                                                    'div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/'
                                                                    'div/div[2]/div[1]/div/div/div/div/div/div/div/div'
                                                                    '/div/div/div/div[1]/div/div/div/div/div/div[2]/div'
                                                                    '/div/div/div/span')
        post_description.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up "
                                   f"when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        time.sleep(2)

        post_description_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main'
                                                                           '/div/div/div/div[1]/div/div[3]/div/div[2]/'
                                                                           'div[1]/div/div/div/div[2]/div[2]/div[2]/div'
                                                                           '/div/div/button')
        post_description_button.click()


twitter_bot = InternetSpeedTwitterBot()
twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()


