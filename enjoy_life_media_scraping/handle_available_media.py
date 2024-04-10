from os import makedirs
from os.path import join
from shutil import copy
from sys import argv
from enjoy_life_media_scraping.model.metadata import Metadata
from enjoy_life_media_scraping.model.section import Section


def handle_available_media(metadata: Metadata, section: Section):
    folder_path = join(argv[1], argv[2], section.title)
    makedirs(folder_path, exist_ok=True)
    copy(metadata.path, folder_path)

