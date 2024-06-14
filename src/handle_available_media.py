from os import isdir, makedirs, rmdir
from os.path import join
from shutil import copy
from sys import argv
from src.model.metadata import Metadata
from src.model.section import Section


def handle_available_media(metadata: Metadata, section: Section):
    folder_path = join(argv[1], argv[2], section.title)
    if isdir(folder_path):
        rmdir(folder_path)
    makedirs(folder_path)
    copy(metadata.path, folder_path)

