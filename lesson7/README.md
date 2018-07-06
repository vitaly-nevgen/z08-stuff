# Lesson 7 Info

## Useful links and info

https://git-scm.com/docs/git-pull
git pull origin master — to pull changes from another branch

https://docs.python.org/3.6/library/os.html#os.listdir
https://docs.python.org/3.6/library/os.path.html#os.path.splitext
или
https://docs.python.org/3/library/stdtypes.html#str.endswith

## About Unix and Windows slashes
/ — Slash (Unix path, e.g. /Users/admin OR web links e.g. http://abc.com/)
\ — Backslash (Windows path, e.g. C:\bla-bla-bla), also used to экранировать символы.

## Hometask

1. Написать программу, которая будет импортировать из файла process_images.py функцию resize_image. 
   Затем программа должна получить список файлов в указанной директории. 
   И каждый файл уменьшить до размера (500х500) или выбранного по желанию. 
1.1. Программа должна положить файлы в другую указанную папку.
1.2. Сделать так, чтобы программа при получении списка файлов отфильтровывала только картинки в JPG формате. 
     То есть папки, другие файлы и пр. не должно попасть в обработку. 