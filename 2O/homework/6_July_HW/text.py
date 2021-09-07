# текстовые файлы
#1) открыть файл  open(file, mode)
# где mode = r чтение, w запись, a дозапись, b бинарный
#2)прочитать read() или записать write()
#3)закрыть файл close()
#newline ="" - не делать дополнительных преобразований символов конца строки
try:
    somefile = open("hello1.txt", "w")
    try:
        somefile.write("hello world")
    except Exception as e:
        print(e)
    finally:
        somefile.close()
except Exception as ex:
    print(ex)
#файл автоматически закрывается
with open("hello2.txt", "w") as somefile:
    somefile.write("hello world")
#дозапись
with open("hello2.txt", "a") as file:
    file.write("\n string 2")
#
with open("hello2.txt", "a") as hello_file:
    print("\n string 3", file=hello_file)
#readline()автоматически вызывается в for для каждой новой строки
with open("hello2.txt", "r") as file:
    for line in file:
        print(line, end="")
#
# open("t1.txt", "r", encoding="utf-8")
with open("hello2.txt", "r") as file:
    str1 = file.readline()
    print(str1, end="")
    str2 = file.readline()
    print(str2)
#чтение до конца файла
with open("hello2.txt", "r") as file:
    line = file.readline()
    while line:
        print(line, end="")
        line = file.readline()
#read() считывает все содержимое файла в одну строку
with open("hello2.txt", "r") as file:
    content = file.read()
    print(content)
#readlines() считывает все строки файла в список
with open("hello2.txt", "r") as file:
    contents = file.readlines()
    str1 = contents[0]
    str2 = contents[1]
    print(str1, end="")
    print(str2)
#явно указать кодировку
filename = "hello2.txt"
with open(filename, encoding="utf8") as file:
    text = file.read()
#вместе
filename = "hello3.txt"
messages = list()
for i in range(4):
    message = "строка " + str(i+1)
    messages.append(message + "\n")
with open(filename, "a",encoding='utf8') as file:
    for message in messages:
        file.write(message)
print("Считанные сообщения")
with open(filename, "r", encoding='utf8') as file:
    for message in file:
        print(message, end="")
#
#CSV
#
import csv
FILENAME = "users.csv"
users = [
    ["Tom", 28],
    ["Alice", 23],
    ["Bob", 34]
]
with open(FILENAME, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(users)
with open(FILENAME, "a", newline="") as file:
    user = ["Sam", 31]
    writer = csv.writer(file)
    writer.writerow(user)
with open(FILENAME, "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0], " - ", row[1])
#словарь
FILENAME = "users2.csv"
users = [
    {"name": "Tom", "age": 28},
    {"name": "Alice", "age": 23},
    {"name": "Bob", "age": 34}
]
with open(FILENAME, "w", newline="") as file:
    columns = ["name", "age"]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    # запись нескольких строк
    writer.writerows(users)
    user = {"name" : "Sam", "age": 41}
    # запись одной строки
    writer.writerow(user)
with open(FILENAME, "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], "-", row["age"])
