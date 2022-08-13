import os
import shutil

user = os.getenv('USER')

def downloadsManager():
    path = f'/home/{user}/Downloads/'

    appFile = ['.tar.gz', '.deb']
    osFile = ['.iso', '.ova']
    imgFile = ['.png', '.jpg', '.jpeg', '.webp']

    with os.scandir(path) as entries:
        for entry in entries:
            for i in  range(len(appFile)):
                # Check for app files
                if entry.name.endswith(appFile[i]):
                    try:
                        shutil.move(path + entry.name, path + 'AppFiles/')
                    except IsADirectoryError:
                        os.mkdir(path + 'AppFiles/')
                        print("Unable to move files to it's directory.Please try again.")
                # Check for os files
                if entry.name.endswith(osFile[i]):
                    try:
                        shutil.move(path + entry.name, path + 'OSFiles/')
                    except IsADirectoryError:
                        os.mkdir(path + 'OSFiles/')
                        print("Unable to move files to it's directory.Please try again.")
                # Check for image files
                if entry.name.endswith(imgFile[i]):
                    try:
                        shutil.move(path + entry.name, path + 'imgFiles/')
                    except IsADirectoryError:
                        os.mkdir(path + 'imgFiles/')
                        run()

def run():
    downloadsManager()

if __name__ == '__main__':
    run()

