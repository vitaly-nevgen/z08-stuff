from PIL import Image, ImageOps
#
size = (128, 128)
#
infile = 'Hello.jpg'

outfile = 'resized.png'

im = Image.open(infile)
im.thumbnail(size)

thumb = ImageOps.fit(im, size, Image.ANTIALIAS)

thumb.save(outfile, "PNG")
