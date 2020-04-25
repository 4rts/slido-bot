from selenium import webdriver
import time
import sys

class Bot:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path='/home/ego/Downloads/geckodriver-v0.26.0-linux64/geckodriver')

    def closeBrowser(self):
        self.driver.close()

    def vote(self):
        driver = self.driver
        driver.get("https://app.sli.do/event/wwr2xfuj/live/questions")
        time.sleep(1)
        click_elem = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/sda-live[1]/div[1]/sda-questions[1]/sda-question-list[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/button[1]")
        click_elem.click()

# hash # xpath # times
if __name__ == "main":

    for i in range(0, sys.argv[2]):
        BOT = Bot()
        BOT.vote()
        BOT.closeBrowser()
        print("Done! Next round: " + str(i + 1))