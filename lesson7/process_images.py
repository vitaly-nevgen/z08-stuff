import json
import os.path
from PIL import Image, ImageOps


def get_jobs():
    jobs_file = 'jobs.json'
    f = open(jobs_file, 'r')
    jobs = json.load(f)
    return jobs


def resize_image(infile, outfile, size):
    im = Image.open(infile)
    im.thumbnail(size)
    thumb = ImageOps.fit(im, size, Image.ANTIALIAS)
    thumb.save(outfile, "JPEG")


jobs = get_jobs()

for job in jobs:
    filename = job['filename']

    for preview in job['previews']:
        name, ext = os.path.splitext(filename)

        preview_filename = '{name}_{type}{size}{ext}'.format(
            name=name,
            type=preview['type'],
            size=preview['size'],
            ext=ext
        )

        print(preview_filename)