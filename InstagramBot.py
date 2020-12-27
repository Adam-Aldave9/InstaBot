import pynput
import time
import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException


class Bot(unittest.TestCase):
    def __init__(self):
        self.messages = []  # holds messages
        self.repeat = 0  # How many sets of messages sent per time
        self.waitTime = 0  # wait time of spamming so no ban
        self.loginInfo = []
        self.comment = " "
        print("For proper use, you must have google chrome installed with the corresponding chromedriver version")

    def loginInformation(self):
        username = input("Enter your username")
        password = input("Enter your password")
        self.loginInfo = [username, password]

    def getPath(self):  # path to chromedriver
        while True:
            x = input(
                "Copy and paste the path to the chromedriver her(exclude '\chromedriver.exe') ")
            if x == "":
                continue
            break
        
        self.path = x+"\chromedriver"

    def setUp(self):  
        while True:
            try:
                self.driver = webdriver.Chrome(
                    self.path)  
                break
            except Exception as e:
                print(e)
        return super().setUp()

    def retrieveComment(self):
        self.comment = input("Enter the comment you would like to spam: ")

    def test_start(self): 
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.instagram.com/")
        username = self.driver.find_elements_by_tag_name("input")
        for i in range(len(username)):
            username[i].send_keys(self.loginInfo[i])
        button = self.driver.find_elements_by_tag_name("button")
        button[1].click()
        if self.save is "1":
            time.sleep(10)
            button = self.driver.find_element_by_class_name(
                "sqdOP.L3NKy.y3zKF")
            button.click()
        else:
            time.sleep(10)
            button = self.driver.find_element_by_class_name(
                "sqdOP.yWX7d.y3zKF")
            button.click()
        if self.turn is "1":
            time.sleep(5)
            button = self.driver.find_element_by_class_name("aOOlW.bIiDR")
            button.click()
        else:
            time.sleep(5)
            button = self.driver.find_element_by_class_name("aOOlW.HoLwm")
            button.click()

    def test_saveLoginInfo(self):
        while True:
            try:
                print("Save login info?")
                self.save = int(input("Enter 1 for YES || Enter 0 for NO: "))
                if (self.save == 1) or (self.save == 0):
                    break
                else:
                    print("Enter 1 or 0 please")
                    continue
            except ValueError:
                print("Enter a number please")
                continue

    def test_turnOnPostNotifs(self):
        while True:
            try:
                print("Turn on post notifications?")
                self.turn = int(input("Enter 1 for YES || Enter 0 for NO: "))
                if (self.turn == 1) or (self.turn == 0):
                    break
                else:
                    print("Enter 1 or 0 please")
                    continue
            except ValueError:
                print("Enter 1 or 0")
                continue

    def test_commentOnPosts(self):
        keyboard = pynput.keyboard.Controller()
        finishedComments = []
        num = 0
        while True:
            for k in range(4):
                if k % 2 == 0 and k > 0:
                    finishedComments.clear()
                commentAreas = self.driver.find_elements_by_tag_name("textarea")
                for i in range(len(commentAreas)):
                    skip = False
                    try:
                        for j in range(len(finishedComments)):
                            if finishedComments[j] == commentAreas[i]:
                                skip = True
                                break
                        if skip:
                            continue
                        commentAreas[i].send_keys(" ")
                    except ElementNotInteractableException:
                        keyboard.type(self.comment)
                        time.sleep(2)
                        post = self.driver.find_elements_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ' and @type='submit']")
                        for a in range(len(post)):
                            try:
                                if post[a].is_enabled():
                                     post[a].click()
                                     num += 1
                                     print("number of posts commented"+str(num))
                                     time.sleep(2)
                                     break
                            except ElementClickInterceptedException:
                                continue
                            except StaleElementReferenceException:
                                continue
                        finishedComments.append(commentAreas[i])
                        if 10 == num:
                            print("{} comments sent. Ending program".format(num))
                            break
                        continue
                    except StaleElementReferenceException:
                        continue
                if num == 10:
                    break
            if num == 10:
                break
            self.test_scroll()
        self.driver.close()    

           
                
    def test_scroll(self):           
        # Scroll down to bottom
        x = self.driver.execute_script("return window.pageYOffset;")
        y = self.driver.execute_script("return window.pageYOffset;") + 1500
        self.driver.execute_script("window.scrollTo({}, {});".format(x,y))
        # Wait to load page
        time.sleep(5)
    
    def repeat(self):
        x = int(input("Do you want to run the bot again? Enter 1 for YES || Enter 0 for NO"))
        return x

        
                
bot = Bot()
bot.getPath()
bot.test_saveLoginInfo() #edit to include try and catch if user turns on
bot.test_turnOnPostNotifs() #edit to include try and catch if user turns on
bot.loginInformation()
while True:
    bot.retrieveComment()
    bot.setUp()
    bot.test_start()
    bot.test_commentOnPosts()
    if bot.repeat() == 1:
        continue
    else:
        print("Thank you for using this bot")
        print("exiting")
        break

    




