from PIL import Image, ImageOps
#
size1 = (640, 640)
size2 = (320, 320)
#
infile = 'bird.jpg'

outfile_th = 'resized_Bird_640.jpg'
outfile_Ops = 'resized_Bird_320.jpg'

im = Image.open(infile)
im.thumbnail(size1)
im.save(outfile_th, "JPEG")

ops = ImageOps.fit(im, size2, Image.ANTIALIAS)
ops.save(outfile_Ops, "JPEG")