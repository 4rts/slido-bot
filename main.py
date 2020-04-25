from selenium import webdriver
import time
import sys
import getopt

class Bot:
    def __init__(self, hash, xpath, browser):
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


def main():

    try:
        options, args = getopt.getopt(
            sys.argv[1:], "h:x:b:p:v",
            ["hash=", "xpath=", "browser=", "path=", "votes="])
        for name, value in options:
            if name in ('-h', '--hash'):
                HASH = value
            if name in ('-x', '--xpath'):
                XPATH = value
            if name in ('-b', '--browser'):
                BROWSER = value
            if name in ('-p', '--path'):
                PATH = value
            if name in ('-v', '--votes'):
                VOTES = value

    except getopt.GetoptError as err:
        print(str(err))
        print("Invalid args!")
        sys.exit(1)
    for i in range(1, sys.argv[2] + 1):
        BOT = Bot(HASH, XPATH, BROWSER)
        BOT.vote()
        BOT.closeBrowser()
        print("Votes: " + str(i))
if __name__ == "main":
    main()