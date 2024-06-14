from json import JSONDecodeError
from os import makedirs
from os.path import isfile, join
from typing import Optional
from src.constants.file_path import CACHE_FOLDER_PATH

class FileReadWriteHelper:

    @staticmethod
    def write_to_file(file_name: str, data: str) -> bool:
        try:
            makedirs(CACHE_FOLDER_PATH, exist_ok=True)
            with open(join(CACHE_FOLDER_PATH, file_name), "w", encoding="utf-8") as writer:
                writer.write(data)
            return True
        except JSONDecodeError:
            return None

    @staticmethod
    def read_from_file(file_name: str) -> Optional[str]:
        full_path_file = join(CACHE_FOLDER_PATH, file_name)
        if not isfile(full_path_file):
            return None
        try:
            with open(full_path_file, "r", encoding="utf-8") as writer:
                return writer.read()
        except JSONDecodeError:
            return None
