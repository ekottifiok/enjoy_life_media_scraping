from sys import argv
from typing import List
from enjoy_life_media_scraping.model.section import Section


def handle_summary(sections: List[Section]):
    print("\nSummary:")
    for section in sections:
        print(f"{section.title}")
        print("Not avaiable media:")
        for item in section.not_available_media:
            print(f"\t{item}")
        print(f"\nAvaiable media {len(section.available_media)} copied to {argv[2]}")
