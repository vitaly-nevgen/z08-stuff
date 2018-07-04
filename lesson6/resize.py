from PIL import Image

size = (128,128)

infile = 'cocktail_318-54938.jpg'
outfile = 'resized.png'

im = Image.open(infile)
im.thumbnail(size)
im.save(outfile, "PNG")