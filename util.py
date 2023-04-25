import os


def syncDir():
    if not os.path.exists("temp"):
        os.makedirs("temp")
