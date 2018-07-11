import os.path
from PIL import Image, ImageOps

def resize_image (infile, outfile, size, preview_type):
    size_tuple = (size, size)
    im = Image.open(infile)

    if preview_type == 'thumbnail':
        im.thumbnail(size_tuple)
    elif preview_type == 'fit':
        im = ImageOps.fit(im, size_tuple, Image.ANTIALIAS)å

    # if not os.path.exists(dest_dir):
    #     os.makedirs(dest_dir)

    im.save(outfile, "JPEG")


