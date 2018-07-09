# Lesson 6

## Useful links and info

**PIP Python Package Manager Manual:**  
https://pip.pypa.io/en/stable/

**Installation of Pillow package:**
Insure that virtual environment is activated (you should see `(env)` prefix in Terminal)  
pip3 install Pillow  
or  
pip3 install <**package-name**>

**Pillow links:**  
[PIL.ImageOps.fit](https://pillow.readthedocs.io/en/3.1.x/reference/ImageOps.html?highlight=fit#PIL.ImageOps.fit) — уменьшить и поместить в квадрат
[Image.thumbnail](https://pillow.readthedocs.io/en/3.1.x/reference/Image.html?highlight=Image.thumbnail#PIL.Image.Image.thumbnail) — уменьшить пропорционально  
[Pillow Handbook Tutorial](https://pillow.readthedocs.io/en/3.1.x/handbook/index.html) — для тех, кто хочет углубиться в работу с этой библиотекой.

**Decorators in Python:**
https://realpython.com/primer-on-python-decorators/#decorators (вообще рекомендую всю статью прочитать)

## Hometask:

1. Написать программу, которая из одной картинки делает две уменьшенных превью — одну 640x640px (метод thumbnail), а другую 300x300 (метод ImageOps.fit).  

* 1.1. Модифицировать программу, чтобы она автоматически назначала имя для результирующих файлов.   
Например: на вход получили название файла `image.jpg`, а в результате программа создаст `image_thumbnail640.jpg` и `image_fit300.jpg`. 
2. `**`Написать программу, которая читает из JSON файла структуру вида:
```json
[{
	"filename": "hello.jpg",
	"previews": [
	   {
         "size": 200,
         "type": "fit"
	   },
	  {
        "size": 640,
        "type": "thumbnail"
	  }
	]
}]
```
Где лежит массив с файлами, которые нужно обработать. В каждом описании файла в ключе `previews` хранится список превью, которые нужно сгенерировать.   
`previews.type` — вид превью (fit или thumbnail)  
`previews.size` — размер превью.  
На выходе, как и в задании 1.1, нужно чтобы результирующие файлы назывались по формату `<name>_<type><size>.jpg`.  

3. Разобраться с работой декораторов в Python. Попробовать свои примеры оборачивания функций.