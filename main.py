from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 
from selenium.common.exceptions import ElementClickInterceptedException
from dotenv import load_dotenv
import os
import os
import os
load_dotenv()
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')
ACCOUNT_NAME="choose any page you love and make a follower from it"
class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(5)
        your_user_name=self.driver.find_element(By.NAME, "username")
        your_password=self.driver.find_element(By.NAME, "password")
        your_user_name.send_keys(email)
        your_password.send_keys(password)
        your_password.send_keys(Keys.ENTER)
        time.sleep(10)
        save_account=self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_account:
            save_account.click()
        # click on not now
        time.sleep(5)
        #click on not allow notifications
        not_now=self.driver.find_element(by=By.XPATH, value="// button[contains(text(), 'Not Now')]")
        if not_now:
            not_now.click()
            time.sleep(5)


        
    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{ACCOUNT_NAME}/followers")
        time.sleep(5)
        #this will shows the follower change every time 
        xpath="/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        followers=self.driver.find_element(by=By.XPATH, value=xpath)
        #scroll down the page to get more followers by using some script
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers)
            time.sleep(5)
    def follow(self):
         all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')
         for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()
bot=InstaFollower()
bot.login()
