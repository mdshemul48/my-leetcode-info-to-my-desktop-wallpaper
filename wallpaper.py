from os import path, getenv, getcwd
from ctypes import windll
from shutil import copyfile
from PIL import Image
from tempfile import NamedTemporaryFile


class Wallpaper:
    # Get
    @staticmethod
    def get(returnImgObj=False):
        currentWallpaper = getenv(
            'APPDATA') + "\\Microsoft\\Windows\\Themes\\TranscodedWallpaper"
        if returnImgObj == True:
            return Image.open(currentWallpaper)
        else:
            tempFile = NamedTemporaryFile(mode="wb", suffix='.jpg').name
            copyfile(currentWallpaper, tempFile)
            return tempFile

    # Set
    @staticmethod
    def set(wallpaperToBeSet):
        # Check it is a file
        if path.isfile(wallpaperToBeSet):
            wallpaperToBeSet = path.abspath(wallpaperToBeSet)
            # If a JPG, set
            if wallpaperToBeSet.lower().endswith('.jpg') or wallpaperToBeSet.lower().endswith('.jpeg'):
                windll.user32.SystemParametersInfoW(
                    20, 0, path.abspath(wallpaperToBeSet), 3)
                return True
            # If not a JPG, convert and set
            else:
                image = Image.open(wallpaperToBeSet)
                with NamedTemporaryFile(mode="wb", suffix='.jpg') as tempFile:
                    image.save(tempFile, quality=100)
                    windll.user32.SystemParametersInfoW(
                        20, 0, path.abspath(tempFile), 3)
                return True

        # Check it is a Pillow object
        elif str(wallpaperToBeSet).find('PIL'):
            with NamedTemporaryFile(mode="wb", suffix='.jpg') as tempFile:
                image.save(tempFile, quality=100)
                windll.user32.SystemParametersInfoW(
                    20, 0, path.abspath(tempFile), 3)
            return True
        else:
            return False

    # Copy
    @staticmethod
    def copy(copyTo=getcwd(), fileName='wallpaper.jpg'):
        return copyfile(Wallpaper.get(), path.join(path.abspath(copyTo), fileName))
