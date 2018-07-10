import os, glob
from lesson7.process_images import resize_image


def gen_new_image_name(image_name, method, size):
    name, ext = os.path.splitext(image_name)
    new_name = '{name}_{method}{size}{ext}'.format(name=name, method=method, size=size, ext=ext)
    return new_name


origin_images_rel_folder = 'origin_images'
processed_images_rel_folder = 'processed_images'
cwd = os.getcwd()

origin_images_folder = os.path.join(cwd, origin_images_rel_folder)
processed_images_folder = os.path.join(cwd, processed_images_rel_folder)

images_paths = glob.glob(origin_images_folder + '\\*.jpg')

method = 'thumbnail'
size = 500

for path in images_paths:
    image_name = os.path.basename(path)
    new_image_name = gen_new_image_name(image_name, method, size)
    new_image_path = os.path.join(processed_images_folder, new_image_name)
    resize_image(path, new_image_path, size, method)





