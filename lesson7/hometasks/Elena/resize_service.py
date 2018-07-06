from PIL import Image, ImageOps


def image_thumb(image_name, size):
    new_image_name = image_name[:-4] + '_thumbnail1.jpg'
    im = Image.open(image_name)
    im.thumbnail(size)
    return im.save(new_image_name, "JPEG")


def image_fit(image_name, size):
    new_image_name = image_name[:-4] + '_fit.jpg'
    im = Image.open(image_name)
    im_fit = ImageOps.fit(im, size, centering=(0.8, 0.0))
    return im_fit.save(new_image_name, "JPEG")

size_th = (640, 640)
size_fit = (300, 300)

infile = 'camomile.jpg'

image_thumb(infile, size_th)
image_fit(infile, size_fit)

