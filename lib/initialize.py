from pathlib import Path
import os

import pyocr

local_tessdata = Path(os.path.expanduser('~/.local/share/tessdata'))
if local_tessdata.is_dir():
    os.environ['TESSDATA_PREFIX'] = str(local_tessdata)
    # print('Improved')

available_tools = pyocr.get_available_tools()
# print(available_tools)
# assert len(available_tools) == 1
ocr = available_tools[0]
