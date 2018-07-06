from PIL import Image, ImageOps
a = int(input("Введите желаемый размер изображения "))
b = int(input("Введите желаемый размер изображения"))
size = (a, b)

infile = 'jeepg133.jpg'
outfile = str(a) + "X" + str(b) + infile
im = Image.open(infile)
im.thumbnail(size)
thumb = ImageOps.fit(im, size, )
thumb.save(outfile)




c = int(input("Введите желаемый размер изображения "))
d = int(input("Введите желаемый размер изображения"))
size = (c, d)
infile = 'jeepg133.jpg'
outfile1 = str(a) + "X" + str(b) + infile




im = Image.open(infile)
im.thumbnail(size)
im.save(outfile1)