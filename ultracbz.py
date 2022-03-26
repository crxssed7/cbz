import os
import sys
from shutil import make_archive

def main(path, name, chp_name):
    # Get all the files in the directory
    if os.path.exists(path):
        if os.path.isdir(path):
            make_archive(name + ' ' + chp_name, "zip", path)
            os.rename(name + ' ' + chp_name + '.zip', name + ' ' + chp_name + '.cbz')
    else:
        print('That is not a valid directory')

if __name__ == '__main__':
    path = input("Enter the path to a directory of chapters: ")
    name = input("Enter the name of the manga series: ")
    # Get all of Komi chapters
    dirs = os.listdir(path)
    for _dir in dirs:
        main(os.path.join(path, _dir), name, _dir)
        print(_dir)