from json import dumps
from re import search
from typing import Dict, Optional

from src.model.language import Language
from src.model.metadata import Metadata
from src.helper.string_helper import StringHelper


class FolderMetadata:
    _data: Dict[str, Metadata] = {}

    def add_metadata(self, metadata: Metadata) -> None:
        self._data[metadata.title] = metadata

    def get_metadata(self, language_short_name: str, title: str, duration: str) -> Optional[Metadata]:
        if (title in self._data):
            return self._data[title]
        removed_last_word_flag = False
        modified_title = title
        while True:
            pattern = r'\b' + title + r'\b'
            modified_pattern = r'\b' + modified_title + r'\b'
            for metadata in self._data.values():
                if (search(pattern, metadata.title) or search(modified_pattern, metadata.title)) and \
                    f"_{language_short_name}_" in metadata.path and \
                        ((not removed_last_word_flag) or duration == metadata.duration):
                    return metadata
            title = StringHelper.remove_last_word(title)
            modified_title = StringHelper.remove_first_word(title)
            removed_last_word_flag = True
            if title == modified_title:
                break
        return None

    def to_json(self) -> str:
        return [i.to_json() for i in self._data.values()]
