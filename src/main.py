from time import time
from typing import List
from src.handle_download_media import handle_download_sections
from src.get_metadata import get_folder_metadata
from src.handle_sections import handle_sections
from src.handle_summary import handle_summary
from src.init import init
from src.model.folder_metadata import FolderMetadata
from src.model.language import Language
from src.handle_select_language import handle_select_language
from src.model.section import Section


def main():
    init()

    language: Language = handle_select_language()
    start_time = time()
    folder_data: FolderMetadata = get_folder_metadata()
    end_time = time()
    execution_time = round(end_time - start_time, 2)
    print(f"Done getting the folder metadata. Took: {execution_time} seconds")

    start_time = time()
    print("Starts handling sections.")
    sections: List[Section] = handle_sections(folder_data, language)
    end_time = time()
    execution_time = round(end_time - start_time, 2)

    handle_summary(sections)
    print(f"Done handling sections. Took: {execution_time} seconds")

    handle_download_sections(sections)

    print("\nGoodbye friend\n")

if __name__ == "__main__":
    main()
