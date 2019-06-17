# 1. Написать программу, которая будет импортировать из файла process_images.py функцию resize_image.
# Затем программа должна получить список файлов в указанной директории.
# И каждый файл уменьшить до размера (500х500) или выбранного по желанию.
# 1.1. Программа должна положить файлы в другую указанную папку.
# 1.2. Сделать так, чтобы программа при получении списка файлов отфильтровывала только картинки в JPG формате.
# То есть папки, другие файлы и пр. не должно попасть в обработку.

from PIL import Image, ImageOps

import os
import processimages

source_dir = 'Images_fol_old/'
destination_dir = 'Images_fol_new/'
new_im_list = []

size = 200
preview_type = 'thumbnail'

image_list = os.listdir(source_dir)
os.chdir(source_dir)

for image in image_list:
    image_s, ext = os.path.splitext(image)

    preview_filename = '{name}_{type}{size}{ext}'.format(
        name=image_s,
        type='thumbnail_',
        size=str(size),
        ext=ext
    )
    new_im_list.append(preview_filename)
    processimages.resize_image(image, preview_filename, size, preview_type,)
# os.chdir("..")

