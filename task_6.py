from glob import glob
from PIL import Image
import time


def rename_file(filename_old):
    dot_number = filename_old.rindex(".")
    extension = filename_old[dot_number:]
    time_now = time.strftime("_%d.%m.%Y.%H.%M", time.localtime())
    filename_new = filename_old.replace("new_photo", "rendered_photo")
    filename_new = filename_new.replace(extension, time_now + extension)
    return filename_new


list_file = glob("new_photo/*")
for file in list_file:
    with Image.open(file) as picture:
        picture_rendered = picture.convert("L")
    file_rendered = rename_file(file)
    picture_rendered.save(file_rendered)
