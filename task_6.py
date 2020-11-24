from glob import glob
from PIL import Image
import time
import os


def rename_file(filename_old, tag):
    dot_number = filename_old.rindex(".")
    extension = filename_old[dot_number:]
    time_now = time.strftime("_%d.%m.%Y.%H.%M", time.localtime())
    filename_new = filename_old.replace("new_photo", "rendered_photo")
    filename_new = filename_new.replace(extension, tag + time_now + extension)
    return filename_new


def rendering_file(file, tag):
    size_2_MB = 2 * 2**20
    temporary_file = file.replace("new_photo\\", "temporary_")
    with Image.open(file) as picture:
        if tag == "":
            picture.save(temporary_file)
            while (os.stat(temporary_file).st_size > size_2_MB):
                wigth, height = picture.size
                picture = picture.resize((int(wigth/2), int(height/2)), Image.ANTIALIAS)
                picture.save(temporary_file)
            os.remove(temporary_file)
        picture_rendered = picture.convert("L")
    return picture_rendered


def checking_file(file):
    size_3_MB = 3 * 2**20
    tag = ""
    if os.stat(file).st_size < size_3_MB:
        tag = "SM"
    return tag


list_file = glob("new_photo/*")
for file in list_file:
    tag = checking_file(file)
    picture_rendered = rendering_file(file, tag)
    file_rendered = rename_file(file, tag)
    picture_rendered.save(file_rendered)
