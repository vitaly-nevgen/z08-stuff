import json
import os
import os.path

from PIL import Image, ImageOps
#import os, sys

os.path.join("C:/Users/danutamikhailova/PycharmProjects/z08-stuff/lesson7/homework7/my_images")

#source_dir = '/Users/danutamikhailova/PycharmProjects/z08-stuff/lesson7/homework7/my_images'
#destination_dir = '/Users/danutamikhailova/PycharmProjects/z08-stuff/lesson7/homework7/my_images_converted'

#1.1 resize each image in the directory
def get_jobs_hw():
    jobs_file = 'jobs_hw.json'
    f = open(jobs_file, 'r')
    jobs = json.load(f)
    return jobs

#1. importing images from directory my_images

path = "/Users/danutamikhailova/PycharmProjects/z08-stuff/lesson7/homework7/my_images"
dirs = os.listdir(path)

for file in dirs:
    print(file)

def resize_image(infile, outfile, size, preview_type):
    size_tuple = (size, size)
    im = Image.open(infile)

    if preview_type == 'thumbnail':
        im.thumbnail(size_tuple)
    elif preview_type == 'fit':
        im = ImageOps.fit(im, size_tuple, Image.ANTIALIAS)

    im.save(outfile, "JPEG")


print(get_jobs_hw())

if __name__ == '__main__':
    jobs = get_jobs_hw()

    for job in jobs:
        dir_name = job['dir_name']
        print(dir_name)

        for preview in job['previews']:
            name, ext = os.path.splitext(dir_name)
            preview_file_name = '{name}_{type}{size}{ext}'.format(
                name=name,
                type=preview['type'],
                size=preview['size'],
                ext=ext
            )

            resize_image(dir_name, preview_file_name, preview['size'], preview['type'])
            print(dir_name, preview_file_name,preview['size'], preview['type'])

#1.1 show destination directory

destination_dir = '/Users/danutamikhailova/PycharmProjects/z08-stuff/lesson7/homework7/my_images_converted'

#hw condition 1.2 - only jpg
imgs = []

valid_images = [".jpg"]
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
        continue
    imgs.append(Image.open(os.path.join(path,f))



