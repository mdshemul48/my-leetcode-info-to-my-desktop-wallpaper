import requests


def fetchLeetCodeProfile():
    data = requests.get("https://leetcode.com/mdshemul48/")
    print(data.text)
    pass


if __name__ == "__main__":
    fetchLeetCodeProfile()
