# Lesson 9
**13 July 2018**

## Userful links

**Singletons in python**:\
https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python

**Rich comparison methods**:\
[`https://docs.python.org/3.6/reference/datamodel.html#object.__lt__`](https://docs.python.org/3.6/reference/datamodel.html#object.__lt__)

## Hometask
1. Создать класс Figure, в котором будет пустой метод `.get_area()`.\
1.2. Создать два класса — Circle и Rectangle, которые будут наследоваться от класса Figure.\
1.3. Класс Circle в методе инициализации должен принимать радиус,
а класс Rectangle в инициализации должен принимать значение стороны a и b.\
1.4. Оба класса Circle и Rectangle должны переопределять метод `.get_area()` из класса Figure. (*super вызвать не нужно*).
Этот метод `.get_area()` должен считать площадь по формуле, в зависимости от того, из какого класса вызван метод.

2. Реализовать методы `__lt__`, `__gt__`, и прочие из списка rich comparison methods
(`https://docs.python.org/3.6/reference/datamodel.html#object.__lt__`),
которые бы сравнивали две фигуры по площади, которая бы получалась из метода get_area.
Методы `__lt__`, `__gt__` должны быть объявлены в классе Figure.

   I expect to see following code working in tasks 1 and 2:

   ```python
   circle = Circle(5)
   rect = Rectangle(10, 20)

   if circle > rect:
       print('Circle has greater area than rectangle')
   else:
       print('Rectangle has greater area than circle')

   print(circle.get_area()) # returns 78.5
   print(rect.get_area()) # returns 200
   ```


3. `**`\
    3.1. Создать еще класс Triangle *(так, для развлечения)*, который будет запрашивать длины трех сторон (`a`, `b` и `c`).
    В этом классе также нужно реализовать подсчет площади, например это можно сделать по формуле Герона.\
    3.2. Создать класс-синглтон FiguresRegistry, который будет иметь следующие методы:\
        — `.add(instance)`: это метод, который должен вызываться каждый раз, когда создается новый экземпляр какой либо фигуры.
          То есть необходимо запихнуть вызов `FiguresRegistry().add()` в метод `Figure.__init__`.\
        — `.get_list(type)`: это метод, который должен возвращать список инстансов по конкретному типу.
          То есть вызывая `FiguresRegistry().get_list(Circle)` должен возвращаться список всех Circle, которые были инстанциированы.

    **Хранить списки элементов нужно внутри инстанса FiguresRegistry.**

    `+` Класс-синглтон — это класс, который имеет только один экземпляр. Гуглите `python create singleton`.
    Причина, по которой FiguresRegistry должен быть синглтоном — чтобы у вас по всему коду использовался только один реестр с фигурами.

    `+` Как вы могли заметить, я писал что метод `.add(instance)` имеет только один аргумент `instance`. То есть тип элемента (чтобы понять, в какой список его добавить) вы должны определить по самому элементу, а не передавать вручную.

   I expect to see following additional code working in task 3:

   ```python
   circle1 = Circle(5)
   circle2 = Circle(8)
   rect = Rectangle(10, 20)
   triangle = Triangle(5, 8, 10)

   print(FiguresRegistry().get_list(Circle)) # returns [<Circle>, <Circle>]
   print(FiguresRegistry().get_list(Rectangle)) # returns [<Rectangle>]
   print(FiguresRegistry().get_list(Triangle)) # returns [<Triangle>]
   ```


   Additionally you can implement following methods:
   ```python
   print(Circle.get_list()) # returns [<Circle>, <Circle>]
   print(Rectangle.get_list()) # returns [<Rectangle>]
   print(Triangle.get_list()) # returns [<Triangle>]
   ```



4. `*****` \
    TODO: я еще добавлю файл с тестами, которые должна уметь проходить ваша программа.
    Убедитесь, что в вашей программе есть проверка на `__name__ == '__main__'` чтобы тесты могли нормально импортировать ваши классы.
    Разумеется, что в тесте нужно будет указать правильный путь для импортирования вашего файла с реализациями классов.




