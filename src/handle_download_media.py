from typing import List
from src.model.section import Section
from asyncio import get_event_loop


def handle_download_sections(sections: List[Section]):

    while True:
        user_input = input("Do you want to download the missing media. y/n: ")
        user_input= user_input.lower()
        if (user_input == 'y' or user_input == 'yes'):
            for section in sections:
                 get_event_loop().run_until_complete(section.download_media())

        elif (user_input == 'n' or user_input == 'no'):
            return
        else:
            print("Please enter a valid input.")
            pass
