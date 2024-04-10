from sys import argv
from typing import List
from enjoy_life_media_scraping.model.section import Section


def handle_summary(sections: List[Section]):
    print("Summary:")
    for section in sections:
        print(f"\t{section.title}")
        print("\t\tNot avaiable media:")
        for item in section.not_available_media:
            print(f"\t\t\t{item}")
        print(f"\n\t\tAvaiable media {len(section.available_media)} copied to {argv[2]}")
        # for item in section.available_media:
        #     print(f"\t\t\t{item}")