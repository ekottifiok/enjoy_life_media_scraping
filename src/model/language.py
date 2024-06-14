from typing import List


class Language:
    def __init__(self, short_name: str, long_name: str, links: List[str]):
        self.short_name = short_name
        self.long_name = long_name
        self.links = links
