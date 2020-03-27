#!/usr/bin/python3

import os
from pathlib import Path
import subprocess


upPath = Path("./static/upside/")

picOutBase = Path("./static/covers")

for (dirpath, dirnames, filenames) in os.walk(upPath):
    if item.suffix == ".mp4":
        subprocess.call(
            [
                "ffmpeg",
                "-y",
                "-i",
                item,
                "-ss",
                "00:00:05.000",
                "-vframes",
                "1",
                picOutBase / item.name,
            ]
        )
