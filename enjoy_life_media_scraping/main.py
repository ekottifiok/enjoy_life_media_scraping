from time import time
from typing import Dict, List
from enjoy_life_media_scraping.get_metadata import get_folder_metadata
from enjoy_life_media_scraping.handle_section import handle_section
from enjoy_life_media_scraping.handle_summary import handle_summary
from enjoy_life_media_scraping.init import init
from enjoy_life_media_scraping.model.metadata import Metadata
from enjoy_life_media_scraping.model.section import Section

def main():
    init()

    links = [
        'https://www.jw.org/en/library/books/enjoy-life-forever/section-1/media/',
        'https://www.jw.org/en/library/books/enjoy-life-forever/section-2/media/',
        'https://www.jw.org/en/library/books/enjoy-life-forever/section-3/media/',
        'https://www.jw.org/en/library/books/enjoy-life-forever/section-4/media/',
    ]

    start_time = time()
    folder_data: Dict[str, Metadata] = get_folder_metadata()
    end_time = time()
    execution_time = round(end_time-start_time, 2)
    print(f"Done getting the folder metadata. Took: {execution_time} seconds")

    result: List[Section] = []
    start_time = time()
    print("Starts handling sections.")
    for index, link in enumerate(links):

        section = Section(link, f'Section {index+1}')
        print(f"Start reading {section.title}")
        section = handle_section(section, folder_data)
        result.append(section)
        print(f"Done handling {section.title}")

    end_time = time()
    execution_time = round(end_time-start_time, 2)

    handle_summary(result)
    print(f"Done handling sections. Took: {execution_time} seconds")


if __name__ == "__main__":
    # Pass the file path to the function
    main()
