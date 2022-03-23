import os
import sys
from shutil import make_archive

def main(path):
    # Get all the files in the directory
    chp_name = os.path.basename(path)
    name = input("What is the name of the comic? ")
    make_archive(name + ' ' + chp_name, "zip", path)
    os.rename(name + ' ' + chp_name + '.zip', name + ' ' + chp_name + '.cbz')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('Invalid usage\nYou need to pass the path to where the comic pages are stored')