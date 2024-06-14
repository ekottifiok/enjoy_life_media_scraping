# Enjoy Life Media Scraping

This package helps arrange all the media files in you computer based on what is available online

- [Enjoy Life Media Scraping](#enjoy-life-media-scraping)
  - [About](#about)
  - [Screenshots](#screenshots)
  - [Getting Started](#getting-started)
  - [Translation](#translation)

## About

This program scrapes the webpage of the Enjoy Life Media page and checks if you have the video on your computer. If you have it, it arranges it in you computer. So that you can copy it freely section by section.

## Screenshots

![Screenshot of the terminal showing the code in action](screenshots/Screenshot%20(132).png) {height: "300px}
![Screenshot of the terminal showing the code in action continued](screenshots/Screenshot%20(133).png) {height: "300px}

## Getting Started

1. Install python and poetry
2. Install dependencies necessary `poetry install`
3. Run the program `poetry run main [videos folder] "[name of output folder]"` `poetry run main /e/Library/Videos/JWLibrary "Enjoy Life Videos"`

## Translation

For other languages you would have to edit the links variable in the `src/constants/supported_languages.py` file. You will have to supply the `long_name`, `short_name` and `links`.
