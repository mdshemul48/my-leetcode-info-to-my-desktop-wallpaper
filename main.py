from Scraper import Scraper
from editor import Editor


def main():
    scrap = Scraper()
    scrap.getScreenShortOfRank()
    scrap.getScreenShortOfStatus()
    scrap.getScreenShortOfChart()

    e = Editor("default.jpg")
    e.setAnotherImage("images\\rank.png", (3150, 50))
    e.setAnotherImage("images\\solved.png", (2830, 250))
    e.setAnotherImage("images\\chart.png", (1000, 1600))
    e.save()

    pass


if __name__ == "__main__":
    main()
