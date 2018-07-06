import json
from PIL import Image, ImageOps


# Написать программу, которая из одной картинки делает две уменьшенных превью — одну 640x640px (метод thumbnail), а другую 300x300 (метод ImageOps.fit).
# 1.1. Модифицировать программу, чтобы она автоматически назначала имя для результирующих файлов.
# Например: на вход получили название файла image.jpg, а в результате программа создаст image_thumbnail640.jpg и image_fit300.jpg.

def image_resize(image_name, size, type):
    size = (size, size)
    im = Image.open(image_name)
    original_name = image_name[:-4]
    if type == 'thumbnail':
        new_image_name = original_name + '_' + type + str(size[0]) + '.jpg'
        im.thumbnail(size)
        return im.save(new_image_name, "JPEG")
    elif type == 'fit':
        new_image_name = original_name + '_' + type + str(size[0]) + '.jpg'
        im_fit = ImageOps.fit(im, size, centering=(0.8, 0.0))
        return im_fit.save(new_image_name, "JPEG")
    else:
        return None


# **Написать программу, которая читает из JSON файла структуру,
# где лежит массив с файлами, которые нужно обработать. В каждом описании файла в ключе previews хранится список превью, которые нужно сгенерировать.
# На выходе, как и в задании 1.1, нужно чтобы результирующие файлы назывались по формату <name>_<type><size>.jpg.

f = open('images_description.json', 'r')
file_data = json.load(f)

for image in (0, len(file_data)-1):
    im_name = file_data[image]['filename']
    previews_data = file_data[image]['previews']
    for preview in (0, len(previews_data)-1):
        image_resize(im_name, previews_data[preview]['size'], previews_data[preview]['type'])