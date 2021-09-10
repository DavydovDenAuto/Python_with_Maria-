# Строки - неизменяемые, в кодировке Unicode
# первый символ строки будет иметь индекс 0
# последний символ -1
string = "hello world"
c0 = string[0]  # h
print(c0)
c6 = string[6]  # w
print(c6)
c11 = "старое значение"
# c11 = string[11]  # ошибка IndexError: string index out of range
print(c11)
c1 = string[-1]  # d
print(c1)
c5 = string[-5]  # w
print(c5)
# подстроки
# string[:end] с 0-го индекса по индекс end
# string[start:end] с индекса start по индекс end
# string[start:end:step]: с индекса start по индекс end через шаг step
# с 0 до 5 символа
sub_string1 = string[:5]
print(sub_string1)  # hello
# со 2 до 5 символа
sub_string2 = string[2:5]
print(sub_string2)  # llo
# со 2 по 9 символ через один символ
sub_string3 = string[2:9:2]
print(sub_string3)  # lowr
# числовое значение для символа в кодировке Unicode
print(ord("A"))  # 65
# длина строки
length = len(string)
print(length)  # 11
# поиск подстроки
exist = "hello" in string
print(exist)  # True
exist = "sword" in string
print(exist)  # False
# цикл for
for char in string:
    print(char)
# isalpha(): возвращает True, если строка состоит только из алфавитных символов
# islower(): возвращает True, если строка состоит только из символов в нижнем регистре
# isupper(): возвращает True, если все символы строки в верхнем регистре
# isdigit(): возвращает True, если все символы строки - цифры
# isnumeric(): возвращает True, если строка представляет собой число
# startswith(str): возвращает True, если строка начинается с подстроки str
# endswith(str): возвращает True, если строка заканчивается на подстроку str
# lower(): переводит строку в нижний регистр
# upper(): переводит строку в вехний регистр
# title(): начальные символы всех слов в строке переводятся в верхний регистр
# capitalize(): переводит в верхний регистр первую букву только самого первого слова строки
# lstrip(): удаляет начальные пробелы из строки
# rstrip(): удаляет конечные пробелы из строки
# strip(): удаляет начальные и конечные пробелы из строки
# ljust(width): если длина строки меньше параметра width, то справа от строки добавляются пробелы, чтобы дополнить значение width, а сама строка выравнивается по левому краю
# rjust(width): если длина строки меньше параметра width, то слева от строки добавляются пробелы, чтобы дополнить значение width, а сама строка выравнивается по правому краю
# center(width): если длина строки меньше параметра width, то слева и справа от строки равномерно добавляются пробелы, чтобы дополнить значение width, а сама строка выравнивается по центру
# find(str[, start [, end]): возвращает индекс подстроки в строке. Если подстрока не найдена, возвращается число -1
# replace(old, new[, num]): заменяет в строке одну подстроку на другую
# split([delimeter[, num]]): разбивает строку на подстроки в зависимости от разделителя
# join(strs): объединяет строки в одну строку, вставляя между ними определенный разделитель
#
string = input("Введите число: ")
if string.isnumeric():
    number = int(string)
    print(number)
#
file_name = "hello.py"
starts_with_hello = file_name.startswith("hello")  # True
ends_with_exe = file_name.endswith("exe")  # False
#
string = "   hello  world!  "
string = string.strip()
print(string)  # hello  world!
#
print("iPhone 7:".ljust(15), "|", "52000".rjust(10))
print("Huawei P10:".ljust(15), "|", "36000".rjust(10))
# поиск. Если подстрока не найдена, find возвращает -1
welcome = "Hello world! Goodbye world!"
index = welcome.find("wor")
print(index)  # 6
# поиск с 10-го индекса
index = welcome.find("wor", 10)
print(index)  # 21
# поиск с 10 по 15 индекс
index = welcome.find("wor", 10, 15)
print(index)  # -1
# replace(old, new): заменяет подстроку old на new
# replace(old, new, num): параметр num указывает,
# сколько вхождений подстроки old надо заменить на new
phone = "+1-234-567-89-10"

# замена дефисов на пробел
edited_phone = phone.replace("-", " ")
print(edited_phone)  # +1 234 567 89 10

# удаление дефисов
edited_phone = phone.replace("-", "")
print(edited_phone)  # +12345678910

# замена только первого дефиса
edited_phone = phone.replace("-", "", 1)
print(edited_phone)  # +1234-567-89-10
# split() разбивает строку на список подстрок
# В качестве разделителя может выступать любой символ или последовательность символов
# split(): в качестве разделителя используется пробел
# split(delimeter): в качестве разделителя используется delimeter
# split(delimeter, num): параметр num указывает, сколько вхождений delimeter используется для разделения. Оставшаяся часть строки добавляется в список без разделения на подстроки
text = "Это был огромный, в два обхвата дуб, с обломанными ветвями и с обломанной корой"
# разделение по пробелам
splitted_text = text.split()
print(splitted_text)
print(splitted_text[6])  # дуб,

# разбиение по запятым
splitted_text = text.split(",")
print(splitted_text)
print(splitted_text[1])  # в два обхвата дуб

# разбиение по первым пяти пробелам
splitted_text = text.split(" ", 5)
print(splitted_text)
print(splitted_text[5])  # обхвата дуб, с обломанными ветвями и с обломанной корой
# join(): он объединяет список строк. Причем текущая строка, у которой вызывается данный метод, используется в качестве разделителя:
words = ["Let", "me", "speak", "from", "my", "heart", "in", "English"]

# разделитель - пробел
sentence = " ".join(words)
print(sentence)  # Let me speak from my heart in English

# разделитель - вертикальная черта
sentence = " | ".join(words)
print(sentence)  # Let | me | speak | from | my | heart | in | English
# можно передать простую строку, тогда разделитель
# будет вставляться между символами этой строки
word = "hello"
joined_word = "|".join(word)
print(joined_word)  # h|e|l|l|o

# вывод в виде таблицы
print('{:10s} {:3d}  {:7.2f}'.format('x', 123, 98))
print('{:10s} {:3d}  {:7.2f}'.format('yyyy', 3, 1.0))
print('{:10s} {:3d}  {:7.2f}'.format('zz', 42, 123.34))