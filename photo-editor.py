import os
from PIL import Image, ImageEnhance, ImageFilter

path = "./imgs" # folder for unedited images
pathOut = "./editedImgs" # folder for edited images

edits = [
    lambda img: img.convert("RGB").filter(ImageFilter.SHARPEN),
    lambda img: img.rotate(-90),
    lambda img: ImageEnhance.Contrast(img).enhance(1.5),
    lambda img: ImageEnhance.Brightness(img).enhance(1.2),
    lambda img: img.resize((int(img.width * 0.5), int(img.height * 0.5))),
    lambda img: img.crop((img.width / 4, img.height / 4, 3 * img.width / 4, 3 * img.height / 4))
]

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    for edit in edits:
        img = edit(img)
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{pathOut}/{clean_name}_edited.jpg')