import os
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from driver.driver import Driver

from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('../.env')
load_dotenv()
load_dotenv(dotenv_path=dotenv_path)


class Login:
    def login(self, driver):
        try:
            # I use environment variable  base on these tutorials https://www.youtube.com/watch?v=IolxqkL7cD8
            username = os.environ.get('facebook_email')
            # username = os.getenv('facebook_email_project')
            # print(username)
            password = os.environ.get('facebook_pass')
            # password = os.getenv('facebook_pass_project')
            # print(password)
            driver.find_element(By.NAME, "email").send_keys(username)
            driver.find_element(By.NAME, "pass").send_keys(password)
            driver.find_element(By.NAME, "login").click()

            print(input("Login work Successfully Press any Key: "))

        except:
            pass


if __name__ == "__main__":
    driver = Driver().driver
    driver.get("https://facebook.com")
    Login().login(driver)
