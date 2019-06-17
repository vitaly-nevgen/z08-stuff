from os import listdir
from os.path import isfile, join

## get list of files (! without dirs) in direct location ##
onlyfiles = [f for f in listdir("/home/julia/Pictures/") if isfile(join("/home/julia/Pictures/", f))]

## process only files with .jpg extention ##
for fname in onlyfiles:
    if fname.endswith(".jpg") == True:
        import process_images as fl
        fl.resize_image('/home/julia/Pictures/'+fname, '/home/julia/Pics/'+fname, 300, 'fit')

## Question:  is it possible to place variable with adress instead "filename.ext" in example below?
## print(os.path.splitext("filename.ext"))
##
