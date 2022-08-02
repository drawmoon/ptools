import os
import sys
from pathlib import Path

from PIL import Image


def isimage(file: str) -> bool:
    img_ext = [".jpg", ".jpeg", ".png"]
    for ext in img_ext:
        if file.lower().endswith(ext):
            return True
    return False


def topdf(filepath: str, outfile: str):
    if os.path.isdir(filepath):
        img_list = []
        for filename in os.listdir(filepath):
            if not isimage(filename):
                continue
            img = Image.open(os.path.join(filepath, filename)).convert("RGB")
            img_list.append(img)
        img_list.pop(0).save(Path.cwd() / outfile, save_all=True, append_images=img_list)
    else:
        img = Image.open(filepath).convert("RGB")
        img.save(Path.cwd() / outfile)


if __name__ == "__main__":
    topdf(sys.argv[1], "export.pdf")
