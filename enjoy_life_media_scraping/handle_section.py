from typing import Dict
from enjoy_life_media_scraping.handle_available_media import handle_available_media
from requests import get, exceptions
from bs4 import BeautifulSoup
from re import match

from enjoy_life_media_scraping.handle_error import handle_error
from enjoy_life_media_scraping.model.metadata import Metadata
from enjoy_life_media_scraping.model.section import Section


def handle_section(section: Section, folder_data: Dict[str, Metadata]) -> Section:
    try:
        response = get(section.link)
    except exceptions.Timeout:
        handle_error('Please check internet connection')

    soup = BeautifulSoup(response.text, 'html.parser')

    tags = soup.select('p > a',)

    for tag in tags:
        text = tag.text
        pattern = r'.+\s+\((\d+:\d+)\)'

        if match(pattern, text):
            splitted = text.split('(')
            title = splitted[0].strip().replace('\u200b', '')
            duration = splitted[1].replace(')', '')

            if title in folder_data:
                section.available_media.append(title)
                handle_available_media(folder_data[title], section)
            else:
                section.not_available_media.append(title)

    return section
