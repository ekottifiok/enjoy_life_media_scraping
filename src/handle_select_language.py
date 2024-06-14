from src.constants.supported_languages import SUPPORTED_LANGUAGES
from typing import List

from src.helper.language_helper import LanguageHelper
from src.model.language import Language


def handle_select_language() -> Language:
    print("Which language you want to scrape")
    for index, language_data in enumerate(SUPPORTED_LANGUAGES):
        language_long_name = language_data["long_name"]
        print(f"\t{index + 1}: {language_long_name}")

    len_links = len(SUPPORTED_LANGUAGES)
    while True:
        try:
            user_input = input("Select which language to scrape or 'q' to quit: ")
            if user_input == 'q':
                exit(0)
            user_input = int(user_input)
            print(len_links)
            if 0 > user_input >= len_links:
                raise Exception(f"Input must be between 1 and {len_links}")
            user_input = user_input - 1
            break
        except Exception as e:
            if e is ValueError:
                print("Please enter a valid number.")
            else:
                print(e)
    return LanguageHelper.from_constant(SUPPORTED_LANGUAGES[user_input])
