from datetime import datetime
from sys import argv
from os import listdir, path
from typing import Dict, Union
from pymediainfo import MediaInfo
import concurrent.futures
from enjoy_life_media_scraping.handle_error import handle_error
from enjoy_life_media_scraping.model.metadata import Metadata


def get_folder_metadata() -> Dict[str, Metadata]:

    folder_path = argv[1]
    try:
        dir_list = listdir(folder_path)
    except:
        handle_error('Failed to find folder path')

    print("Starts reading the metadata in the folder")

    def get_file_metadata(name: str) -> Union[Metadata, None]:
        if not name.endswith(".mp4"):
            return None

        file_path = path.join(folder_path, name)
        media_info = MediaInfo.parse(file_path)

        for track in media_info.tracks:     # type: ignore
            if track.track_type == 'General' and isinstance(track.duration, int):
                t = datetime.fromtimestamp(track.duration/1000)
                if (t.hour == 1):
                    t = t.replace(hour=0)
                formatted_time_string = t.strftime(
                    "%H:%M:%S") if t.hour > 0 else t.strftime("%M:%S")

                return Metadata(
                    formatted_time_string,
                    file_path,
                    track.title,
                )
            return None

    # Create a ThreadPoolExecutor with max_workers as the number of concurrent threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(dir_list)) as executor:

        # Submit the process_data function to the executor for each data item
        future_to_data = {executor.submit(
            get_file_metadata, file): file for file in dir_list}

        # Initialize a list to store the results
        metadata_dict = {}

        # Iterate over the futures as they are completed
        for future in concurrent.futures.as_completed(future_to_data):
            # Get the result from the completed future
            data = future.result()
            if data is not None:
                metadata_dict[data.title] = data

    return metadata_dict
