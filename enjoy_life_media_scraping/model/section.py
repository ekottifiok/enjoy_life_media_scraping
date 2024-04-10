class Section:

    def __init__(self, link: str, title: str) -> None:
        self.link = link
        self.title = title
        self.available_media = []
        self.not_available_media = []
