from pathlib import Path
from typing import Optional
import os
import re

from PIL import Image
import click
import pyocr
import regex

from lib.initialize import ocr

TypePath = click.types.Path(path_type=Path)

mysterious_spaces = regex.compile(r'''(?: [\p{Hiragana}\p{Katakana}\p{Han}] ?)+''')


def remove_mysterious_spaces(s: str) -> str:
    result = []
    last_right = 0
    for it in mysterious_spaces.finditer(s):
        left, right = it.span()
        result.append(s[last_right:left])
        result.append(it.group().replace(' ', ''))
        last_right = right
    result.append(s[last_right:])
    return ''.join(result)


# tesseract_layout - https://valmore.work/how-to-use-tesseract4-with-python/

@click.command()
@click.argument('image_path', type=str, required=True)
@click.argument('layout', type=int, default=12)
@click.argument('lang', type=str, default='jpn')
def main(image_path: str, layout: int, lang: str) -> None:
    image = Image.open(image_path)
    builder = pyocr.builders.TextBuilder(tesseract_layout=layout)
    text = ocr.image_to_string(image, lang='jpn', builder=builder)


if __name__ == "__main__":
    main()
