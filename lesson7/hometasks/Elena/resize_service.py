import json
import os.path
from PIL import Image, ImageOps


# Написать программу, которая из одной картинки делает две уменьшенных превью —
# одну 640x640px (метод thumbnail), а другую 300x300 (метод ImageOps.fit).
# 1.1. Модифицировать программу, чтобы она автоматически назначала имя для результирующих файлов.
# Например: на вход получили название файла image.jpg, а в результате программа
# создаст image_thumbnail640.jpg и image_fit300.jpg.

def image_resize(image_name, size, type, centering):
    image_size = (size, size)
    im = Image.open(image_name)
    name, ext = os.path.splitext(image_name)
    new_image_name = name + '_' + type + str(size) + ext
    if type == 'thumbnail':
        im.thumbnail(image_size)
    else:
        im = ImageOps.fit(im, image_size, method=Image.ANTIALIAS, centering=centering)
    im.save(new_image_name, "JPEG")


# **Написать программу, которая читает из JSON файла структуру,
# где лежит массив с файлами, которые нужно обработать. В каждом описании файла
# в ключе previews хранится список превью, которые нужно сгенерировать.
# На выходе, как и в задании 1.1, нужно чтобы результирующие файлы назывались по формату <name>_<type><size>.jpg.

f = open('images_description.json', 'r')
images = json.load(f)

for image in images:
    im_name = image['filename']
    previews = image['previews']
    for preview in previews:
        size = preview['size']
        preview_type = preview['type']
        centering = preview.get('centering', [0.5, 0.5])
        image_resize(im_name, size, preview_type, centering)