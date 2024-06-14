from sys import argv
from typing import List
from src.model.section import Section


def handle_summary(sections: List[Section]) -> None:
    print("\nSummary:")
    for section in sections:
        section.print_summary()
    print(f"\nAvailable media {sum([len(i.available_media) for i in sections])} copied to {argv[2]}")
