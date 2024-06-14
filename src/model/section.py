from concurrent.futures import ThreadPoolExecutor, as_completed
from json import JSONDecodeError
from typing import Optional
from requests import get, Response
from requests.exceptions import Timeout

from src.helper.file_read_write_helper import FileReadWriteHelper
from src.helper.string_helper import StringHelper
from asyncio import ensure_future, gather, get_event_loop, run
from pyppeteer import launch
from playwright.async_api import async_playwright



class Section:

    def __init__(self, link: str, title: str, language_short) -> None:
        self.link = link
        self.title = title
        self.available_media = []
        self._not_available_media = []
        self._filename = f"{StringHelper.kebab_case(self.title)}_{language_short}_.html"
        self._download_link = []

    def get_section(self) -> Optional[str]:
        if self.load_section():
            return self._data
        try:
            response: Response = get(self.link)
            self._data = response.text
            self.save_section()
            return response.text
        except Timeout:
            print('Please check internet connection')
            return None

    def save_section(self) -> bool:
        result = FileReadWriteHelper.write_to_file(self._filename, self._data)
        if result:
            self._data = result
            print("Successfully saved section data to file")
            return True
        else:
            print("Error: Failed to save section to file")
            return False

    def load_section(self) -> bool:
        result = FileReadWriteHelper.read_from_file(self._filename)
        if result:
            self._data = result
            return True
        else:
            return False

    def add_not_available(self, title: str, link: Optional[str]) -> None:
        self._not_available_media.append(title)
        self._download_link.append(link)

    def print_summary(self) -> None:
        if len(self._not_available_media) == 0:
            return
        print(f"{self.title}")
        print("Not available media:")
        for item in self._not_available_media:
            print(f"\t{item}")
        print(self._download_link)

    async def download_media(self) -> None:
        if len(self._download_link) == 0:
            return
        async def worker(link: str) -> bool:
            async with async_playwright() as p:
                browser = await p.chromium.launch()
                page = await browser.new_page()
                await page.goto(link)
                # await page.screenshot(path=f'example-{p.chromium.name}.png')
                # button = await page.locator(".dropdownHandle")
                # print(button)
                # content = await page.content()
                # print(content)
                # title = await page.title()
                # print(title)
                await browser.close()
            # browser = await launch()
            # page = await browser.newPage()
            # await page.goto('https://example.com')
            # await page.screenshot({'path': 'example.png'})
            # await browser.close()
            # try:
            #     response: Response = get(link, allow_redirects=True)
            #     data = response.text
            # except Timeout:
            #     print('Please check internet connection')
            #     return False
            # soup = BeautifulSoup(data, 'html.parser')
        #     return True
        # for link in self._download_link:

        # with ThreadPoolExecutor(max_workers=len(self._download_link)) as executor:
        #     futures_to_data = {executor.submit(
        #         run, worker(link)
        #     ): link for link in self._download_link}
        #     for future in as_completed(futures_to_data):
        #         result = future.result()
        #         if result:
        #             print(f"Done downloading {future}")
        # async for link in self._download_link:
        #     await worker(link)
        tasks = [
            ensure_future(
                worker(link)
            ) for link in self._download_link[:1]
        ]
        await gather(*tasks)
