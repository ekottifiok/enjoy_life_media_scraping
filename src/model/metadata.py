from src.helper.string_helper import StringHelper


class Metadata:

    def __init__(self, duration: str, path: str, title: str) -> None:
        self.title = title
        self.path = path
        self.duration = StringHelper.remove_leading_zeros(duration)

    def to_json(self):
        return self.__dict__
