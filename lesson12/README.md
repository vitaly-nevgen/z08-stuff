# Lesson 12

## Useful links:

**Репозиторий polls**:\
https://github.com/vitaly-nevgen/tms_polls

**Форматирование времени**:\
http://strftime.org/

**Статус-коды HTTP**:\
https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

**Описание синтаксиса шаблонов Jinja**:\
http://jinja.pocoo.org/

**CSS Tutorial + description**:\
https://en.wikipedia.org/wiki/Cascading_Style_Sheets\
https://www.w3schools.com/css/

**HTML forms**:\
https://www.w3schools.com/html/html_forms.asp

**CSRF**:\
[Межсайтовая подделка запроса](https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D0%B6%D1%81%D0%B0%D0%B9%D1%82%D0%BE%D0%B2%D0%B0%D1%8F_%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D0%BB%D0%BA%D0%B0_%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81%D0%B0)


## Hometask

1. Создать view, который будет отобржать в человеко-читаемом виде список студентов из файла `students.json` (этот файл положить внутрь приложения).
3. Создать view, где будут находиться поля для ввода адреса email, темы и сообщения. Исходя из этих полей чтобы отправлялось письмо.


Для второго задания вам понадобится модуль [smtp](https://docs.python.org/3.6/library/smtplib.html).