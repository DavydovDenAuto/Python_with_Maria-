# динамическая типизация
a = "Привет!"
a = 'Привет!'
print(a)
print(type(a))
a = 2
a += 3  # добавить к старому значению
print(a)
print(type(a))
a = 2.8e-5  # экспоненциальная запись числа
print(a)
print(type(a))
# регистрозависимость
A = 88
print("a= ", a, " A = ", A)

# ввод данных в виде строк
name = input("Введите название: ")
# k = int(input("Введите количество: "))
k = float(input("Введите количество: "))
print("название ", name, " количество ", k)

# арифметические операции
print()
print("2+3=", 2 + 3)
print("2-3=", 2 - 3)
print("2/3=", 2 / 3)
print("2.0/3.0=", 2.0 / 3.0)
print("2.0//3.0=", 2.0 // 3.0)  # отбросить дробную часть
print("2**3=", 2 ** 3)  # возведение в степень
print("8%5=", 8 % 5)  # остаток от деления
a = 2.10101010101
a += 8.0020202
print("a=", a, " round(a, 4)= ", round(a, 4))
g = 123456789
print("g=", g, " round(g, -3)= ", round(g, -3))

# форматный вывод числа
print()
print("{0:07} с пробелами - после двоеточия пробел {0: 7} ".format(25))
print()

# системы исчисления
x2 = 0b101  # 101 в двоичной системе равно 5
x8 = 0o11  # 11 в восьмеричной системе равно 9
x16 = 0x0a  # a в шестнадцатеричной системе равно 10
z = x2 + x8 + x16
print("{0} in binary {0:09b}   in hex {0:03x} in octal {0:03o}".format(z))

# логический операции
# приоритеты: оператор not, затем оператор and, а в конце оператор or
print()
a = 5
b = 8
rez = a > 2 and b < 10
print("a= ", a, " b= ", b, " a>2 and b<10 ", rez)
rez = a > 2 or b < 10
print("a>2 or b<10 ", rez)
rez = (a > 2 and a + b < 100) or b < 5
print("(a>2 and a+b<100) or b<5 ", rez)
rez = not (a > 2 and (a + b < 100 or b < 5))
print("not (a>2 and (a+b<100 or b<5)) ", rez)

# сравнение строк в порядке алфавита с учетом регистра
print()
str1 = "Tom"
str2 = "tom"
print(str1 < str2)
print(str1 == str2)
print(str1.lower() == str2.lower())
# нет операций a++, a--, ++a, --a
# x < y < z эквивалентно x < y and y < z
print("2 < 5 < 8", 2 < 5 < 8)
print("2 < 8 < 5", 2 < 8 < 5)
# separator
x = 1_23_45.67_8
print(x)

name, age, phone = input("имя, возраст, телефон, разделенные пробелами: ").split()
print("Вы ввели: ", name, age, phone)
