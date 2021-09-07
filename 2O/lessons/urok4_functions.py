#определение функции:
def say_hello1():
    print("Hello")
#вызов функции
say_hello1()
# функция с параметрами
def say_hello2(name):
    print("Hello, ",name)
#вызов функции
say_hello2("Tom")
say_hello2("Bob")
say_hello2("Alice")
#значение по умолчанию
def say_hello3(name="Tom"):
    print("Hello,", name)
#вызов функции
say_hello3()
say_hello3("Alice")
#использование именованных параметров
def display_info(name, age):
    print("Name:", name, "\t", "Age:", age)
#вызов функции
display_info("Dik", 18)
display_info(age=22, name="Tom") # наоборот
# С помощью символа звездочки можно
# определить неопределенное количество параметров -
# кортеж (tuple) - подробнее о нем в следующем уроке
def sum(*params):
    result = 0
    for n in params:
        result += n
    return result
#вызов функции
sumOfNumbers1 = sum(1, 2, 3, 4, 5)
sumOfNumbers2 = sum(3, 4, 5)
print(sumOfNumbers1)
print(sumOfNumbers2)
#функция возвращает значение
def exchange(usd_rate, money):
    result = round(money/usd_rate, 2)
    return result
#вызов функции
result1 = exchange(60, 30000)
print(result1)
result2 = exchange(56, 30000)
print(result2)
result3 = exchange(65, 30000)
print(result3)
#функция возвращает сразу несколько значений
def default_user():
    name = "Tom"
    age = 33
    return name, age
#вызов функции
user_name, user_age = default_user()
print("Name:", user_name, "\t Age:", user_age)
#главная функция main, в которой потом уже вызываются другие функции
def main():
    say_hello3("Tom")
# вызов функции main
main()
#глобальная переменная
number = 5

def myfunc():
    #глобальная переменная
    print(number)

def anotherfunc():
    #print(number) # ошибка, т.к. ниже определена
        # локальная переменная number
    number = 3 # локальная переменная
    print(number) # локальная переменная

def yetanotherfunc():
    global number #глобальная переменная
    number = 3 #глобальная переменная
    print(number) #глобальная переменная
# вызов функции
myfunc()
print("global number=", number)
anotherfunc()
print("global number=", number)
yetanotherfunc()
print("global number=", number)

# рекурсия на примере суммы цифр
def recurs_sum(m):
	result=0
	print("test ", m)
	while m>0 :
		x=m%10
		result+=x
		m=m//10
	if result>9:
		result=recurs_sum(result)
	return result

# вызов функции
x=recurs_sum(123456789)
print(x)
# в одном из следующих уроков будет аргумент словарь (dictionary)
# def info(**params):
