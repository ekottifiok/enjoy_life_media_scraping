from re import sub
from typing import Optional


class StringHelper:

    @staticmethod
    def kebab_case(s: str):
        return '-'.join(
            sub(r"(\s|_|-)+", " ",
                sub(r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+",
                    lambda mo: ' ' + mo.group(0).lower(), s)).split())

    @staticmethod
    def remove_last_word(s: str) -> Optional[str]:
        if len(s.split(" ")) == 1:
            return s
        return ' '.join([word for word in s.split()[:-1]])

    @staticmethod
    def remove_first_word(s: str) -> Optional[str]:
        if len(s.split(" ")) == 1:
            return s
        return ' '.join([word for word in s.split()[1:]])

    @staticmethod
    def remove_leading_character(s: str, character: str) -> str:
        if s[0] != character:
            return s
        s = s[1:]
        return StringHelper.remove_leading_zeros(s)

    @staticmethod
    def remove_leading_zeros(s: str) -> str:
        if s[0] == '0':
            return s[1:]
        return s

    @staticmethod
    def sanitize(s: str) -> str:
        s = s.strip().replace('\u200b', '') \
            .replace('\u201c', "\"").replace('\u201d', "\"") \
            .replace('\u2018', "'").replace('\u2019', "'") \
            .replace('\u00A0', " ").replace('-', " ") \
            .replace('_EditMaster', " ").replace("\"", " ") \
            .replace("'", "").replace("—", " ")
        return s
