from sys import argv
from os import listdir, path
from typing import Dict, Optional, Union
from pymediainfo import MediaInfo
import concurrent.futures
from src.handle_error import handle_error
from src.helper.folder_metadata_helper import FolderMetadataHelper
from src.helper.string_helper import StringHelper
from src.model.folder_metadata import FolderMetadata
from src.model.metadata import Metadata
from datetime import datetime


def get_folder_metadata() -> FolderMetadata:
    folder_path = argv[1]
    folder_modified = datetime.fromtimestamp(path.getmtime(folder_path))

    try:
        dir_list: list[str] = listdir(folder_path)
    except:
        handle_error('Failed to find folder path')

    print("Starts reading the metadata in the folder")
    cache_data: Optional[FolderMetadata] = FolderMetadataHelper.load_metadata(
        folder_modified)
    if cache_data:
        print("Read data from cache")
        return cache_data

    def get_file_metadata(name: str) -> Union[Metadata, None]:
        if not name.endswith(".mp4"):
            return None

        file_path = path.join(folder_path, name)
        media_info = MediaInfo.parse(file_path)

        for track in media_info.tracks:  # type: ignore
            if track.track_type == 'General' and isinstance(track.duration, int):
                t = datetime.fromtimestamp(track.duration / 1000)
                if t.hour == 1:
                    t = t.replace(hour=0)
                formatted_time_string = t.strftime(
                    "%H:%M:%S") if t.hour > 0 else t.strftime("%M:%S")

                return Metadata(
                    formatted_time_string,
                    file_path,
                    StringHelper.sanitize(track.title),
                )
            return None

    # Create a ThreadPoolExecutor with max_workers as the number of concurrent threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(dir_list)) as executor:

        # Submit the process_data function to the executor for each data item
        future_to_data = {executor.submit(
            get_file_metadata, file): file for file in dir_list}

        # Initialize a list to store the results
        folder_metadata = FolderMetadata()

        # Iterate over the futures as they are completed
        for future in concurrent.futures.as_completed(future_to_data):
            # Get the result from the completed future
            data = future.result()
            if data:
                folder_metadata.add_metadata(data)

    if not FolderMetadataHelper.save_metadata(folder_modified, folder_metadata):
        print("Error: Failed to write metadata to file")

    return folder_metadata
