from os.path import exists, join
from shutil import rmtree
from sys import argv

from src.handle_error import handle_error


def init():
    if len(argv) != 3:
        handle_error('Please pass 2 arguments folder path and folder name')

    output_path = join(argv[1], argv[2])
    if exists(output_path):
        print('Removing output folder')
        rmtree(output_path)
