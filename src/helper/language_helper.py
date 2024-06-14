from typing import List, Dict, Union

from src.model.language import Language


class LanguageHelper:
    @staticmethod
    def from_constant(data: Dict[str, Union[str, List[str]]]) -> Language:
        if ["links", "long_name", "short_name"] == sorted(data.keys()) \
                and isinstance(data["long_name"], str) \
                and isinstance(data["short_name"], str) \
                and isinstance(data["links"], list) \
                and all(isinstance(item, str) for item in data["links"]):
            return Language(
                short_name=data["short_name"],
                long_name=data["long_name"],
                links=data["links"]
            )
