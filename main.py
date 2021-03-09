import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException
chrome_path = r"C:\Users\Aydin\OneDrive\Υπολογιστής\CodeW\chromedriver.exe"
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
ACCOUNT_NAME = "chefsteps"

class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        accept = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]')
        accept.click()
        time.sleep(1)
        usern = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        passw = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        usern.send_keys(USERNAME)
        passw.send_keys(PASSWORD)
        time.sleep(1)

        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
    def find_followers(self):
        time.sleep(3)
        pth = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        pth.send_keys(ACCOUNT_NAME)
        time.sleep(1)
        pth.send_keys(Keys.ENTER)
        pth.send_keys(Keys.ENTER)
        time.sleep(1)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(1)

        frame = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", frame)
            time.sleep(2)
    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for i in all_buttons:
            try:
                i.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()
user = InstaFollower(chrome_path)
user.login()
user.find_followers()
user.follow()