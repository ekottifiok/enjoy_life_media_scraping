from datetime import datetime
from json import dumps, loads
from sys import argv
from typing import List, Optional

from src.helper.file_read_write_helper import FileReadWriteHelper
from src.model.folder_metadata import FolderMetadata
from src.model.metadata import Metadata


cache_filename = "folder_metadata.json"
cache_header = [
    "date_created",
    "folder_modified",
    "folder_path",
    "metadata"
]


class FolderMetadataHelper:

    @staticmethod
    def get_from_json(data: List[str]) -> Optional[FolderMetadata]:
        folder_metadata = FolderMetadata()
        for item in data:
            if isinstance(item, dict) and \
                    sorted(item.keys()) == ["duration", "path", "title"]:
                folder_metadata.add_metadata(Metadata(**item))
        return folder_metadata

    @staticmethod
    def save_metadata(folder_modified: datetime, folder_metadata: FolderMetadata) -> bool:
        data = {
                    "date_created": datetime.now().isoformat(),
                    "folder_modified": folder_modified.isoformat(),
                    "folder_path": argv[1],
                    "metadata": folder_metadata.to_json()
                }
        write_bool = FileReadWriteHelper.write_to_file(cache_filename, dumps(data))
        if write_bool:
            # print("Successfully saved folder metadata to file")
            return True
        else:
            # print("Error: Failed to save folder metadata to file")
            return False

    @staticmethod
    def load_metadata(folder_modified: datetime) -> Optional[FolderMetadata]:
        read_data = FileReadWriteHelper.read_from_file(cache_filename)
        if not read_data:
            return None
        read_data = loads(read_data)

        if isinstance(read_data, dict) and \
                sorted(read_data.keys()) == cache_header:
            date_read_folder_modified = datetime.fromisoformat(
                read_data["folder_modified"]
            )
            if folder_modified == date_read_folder_modified:
                return FolderMetadataHelper.get_from_json(read_data["metadata"])
            else:
                return None
        else:
            print(f"Error: Failed to load folder metadata")
