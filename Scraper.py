from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from util import syncDir


class Scraper:
    web: webdriver.Chrome = None

    def __init__(self) -> None:

        options = webdriver.ChromeOptions()
        service = Service(ChromeDriverManager().install())

        options.add_argument("--window-size=1920,1080")

        self.web = webdriver.Chrome(service=service, options=options)
        self.web.maximize_window()
        self.web.get("https://leetcode.com/mdshemul48/")

        sleep(5)

        syncDir()

    def getScreenShortOfRank(self):
        element = self.web.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[1]/div/div[1]/div[1]')
        element.screenshot("images/rank.png")

    def getScreenShortOfChart(self):
        element = self.web.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/div[2]/div')
        element.screenshot("images/chart.png")

    def getScreenShortOfStatus(self):
        element = self.web.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/div[1]/div[1]/div')
        element.screenshot("images/solved.png")

    def __del__(self):
        # self.web.close()
        pass


if __name__ == "__main__":
    s = Scraper()
    s.getScreenShortOfRank()
    s.getScreenShortOfChart()
    s.getScreenShortOfStatus()
