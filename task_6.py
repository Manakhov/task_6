from glob import glob
from PIL import Image

list_file = glob("new_photo/*")
print(list_file)
for file in list_file:
    with Image.open(file) as picture:
        picture_rendered = picture.convert("L")
    file_rendered = file.replace("new_photo", "rendered_photo")
    picture_rendered.save(file_rendered)
