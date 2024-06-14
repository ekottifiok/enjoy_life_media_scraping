from typing import List, Optional
from bs4 import BeautifulSoup
from re import match

from src.handle_available_media import handle_available_media
from src.helper.string_helper import StringHelper
from src.model.folder_metadata import FolderMetadata
from src.model.language import Language
from src.model.section import Section
from concurrent.futures import as_completed, ThreadPoolExecutor


def handle_sections(folder_metadata: FolderMetadata, language: Language) -> List[Section]:

    def worker(
        link: str,
        index: int,
    ) -> Optional[Section]:
        section = Section(link, f"Section {index+1}", language.short_name)
        data: str = section.get_section()
        if not data:
            return None

        soup = BeautifulSoup(data, 'html.parser')

        tags = soup.select('p > a',)

        for tag in tags:
            text = tag.text
            pattern = r'.+\s+\((\d+:\d+)\)'

            if match(pattern, text):
                text_split = text.split('(')
                title = StringHelper.sanitize(text_split[0])
                duration = text_split[1].replace(')', '')
                pattern = r'\b' + pattern + r'\b'
                metadata_result = folder_metadata.get_metadata(
                    language.short_name, title, duration)

                if metadata_result:
                    section.available_media.append(title)
                    handle_available_media(metadata_result, section)
                else:
                    section.add_not_available(title, tag.attrs['href'])
                    print(f"{title} not found for {duration}")

        return section

    with ThreadPoolExecutor(max_workers=len(language.links)) as executor:

        # Submit the process_data function to the executor for each data item
        future_to_data = {executor.submit(
            worker,
            link,
            index,
        ): [index, link] for index, link in enumerate(language.links)}

        # Initialize a list to store the results
        result: List[Section] = []

        for future in as_completed(future_to_data):
            # Get the result from the completed future
            section = future.result()
            if section:
                result.append(section)
                print(f"Done handling {section.title}")
    return result
