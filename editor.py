from PIL import Image
from util import syncDir


class Editor:
    def __init__(self, mainWallpaperPath: str) -> None:
        syncDir()
        image = Image.open(mainWallpaperPath)
        self.mainWallpaper = image.copy()

    def setAnotherImage(self, imagePath: str, location: tuple):
        image = Image.open(imagePath)

        scale = 2.3
        size = (int(scale * image.size[0]), int(scale * image.size[1]))
        newImage = image.resize(size)

        self.mainWallpaper.paste(newImage, location)

    def save(self):
        self.mainWallpaper.save("images/wallpaper.jpg", quality=100)


if __name__ == "__main__":
    e = Editor("default.jpg")
    e.setAnotherImage("images\\rank.png", (3150, 50))
    e.setAnotherImage("images\\chart.png", (1000, 1600))
    e.setAnotherImage("images\\solved.png", (2830, 300))
    e.save()
