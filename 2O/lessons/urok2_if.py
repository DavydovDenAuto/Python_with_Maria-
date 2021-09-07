# # if
# age = 22
# if age > 21:
#     print("Доступ разрешен")
#     print("Завершение работы")
# #
# age = 18
# if age > 21:
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещен")
# #
# age = 18
# if age >= 21:
#     print("Доступ разрешен")
# elif age >= 18:
#     print("Доступ частично разрешен")
# else:
#     print("Доступ запрещен")
# # вложенные конструкции if
# age = 18
# if age >= 18:
#     print("Больше 17")
#     if age > 21:
#         print("Больше 21")
#     else:
#         print("От 18 до 21")
#     #
# age = 18
# if age >= 18:
#     print("Больше 17")
# if age > 21:
#     print("Больше 21")
# else:
#     print("От 18 до 21")
#
# # нет оператора switch
# switcher = {
#     1: "January",
#     2: "February",
#     3: "March",
#     4: "April",
#     5: "May",
#     6: "June",
#     7: "July",
#     8: "August",
#     9: "September",
#     10: "October",
#     11: "November",
#     12: "December"
# }
# print(switcher.get(5, "Invalid month"))
# print(switcher.get(15, "Invalid month"))
# # аналог тернарного оператора
# x = 5
# rez = x * 10 if x < 10 else x / 10
# print("x= ", x, " rez= ", rez)
# x = 45
# rez = x * 10 if x < 10 else x / 10
# print("x= ", x, " rez= ", rez)
# x = 5
# y = 4
# maximum = x if x > y else y
# minimum = x if x < y else y
# print("x= ", x, " y= ", y)
# print("maximum ", maximum)
# print("minimum ", minimum)
# #
func_output = None
msg = func_output or "Не было возвращено данных"
print(msg)
