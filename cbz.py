import os
import sys
import random
import string
from shutil import make_archive

def main(path):
    # Get all the files in the directory
    if os.path.exists(path):
        basename = os.path.basename(path)
        chp_name = basename if basename else 'Output ' + ''.join(random.choices(string.ascii_lowercase, k=5))
        make_archive(chp_name, "zip", path)
        os.rename(chp_name + '.zip', chp_name + '.cbz')
    else:
        print('That is not a valid directory')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('Invalid usage\nYou need to pass the path to where the comic pages are stored')