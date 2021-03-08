import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_path = "C:\Users\Aydin\OneDrive\Υπολογιστής\CodeW"
USERNAME = "enriquegheredia94"
PASSWORD = "Kerem4154!"
ACCOUNT_NAME = "chefsteps"

class InstaFollower:
    def __init__(self,path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        pass
    def find_followers(self):
        pass
    def follow(self):
        pass

user = InstaFollower(chrome_path)
user.login()
user.find_followers()
user.follow()