# #цикл while
# choice = "Y"
# i=0
# while choice.lower() == "y":
#     if i>1 :
#         print(i,") ")
#     i+=1
#     print("Привет")
#     choice = input("Для продолжения нажмите Y, а для выхода любую другую клавишу: ")
# print("цикл завешен")
# #
# number = int(input("Введите число: "))
# i = 1
# factorial = 1
# while i <= number:
#     factorial *= i
#     i += 1
# print("Факториал числа ", number, " = ", factorial)
# #
# factorial = 1
# for i in range(1, number+1):
#     factorial *= i
# print("Факториал числа ", number, " = ", factorial)
# i = 1
# # range
# # range(start, stop, step)
# print ( range(4) ) # 0,1,2,3 #stop
# print ( range(4, 8) ) # 4,5,6,7
# print ( range(4, 0, -1) ) # 4, 3, 2, 1
# # цикл for
# for i in range(5):
#     print(i, end=" ")
# print("\n")
# #вложенные циклы
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, sep=" ; ", end="\t")
#     print("\n")
# #бесконечный цикл
# print("Для выхода нажмите Y")
# while True:
#     data = input("Введите число или Y : ")
#     if data.lower() == "y":
#         break  # выход из цикла
#     a = int(data)
#     if a==5:
#         print("continue")
#         continue #пропустить все до конца цикла = перескочить на следующий шаг цикла
#     print("число", a)
# print("цикл завешен")
#
# # многострочный ввод пользователя отсутствует,
# # но можно сделать так
MultiLine = []
while True:
    line = input()
    if line:
        MultiLine.append(line)
    else:
        break
finalText = '\n'.join(MultiLine)
print("Final text input")
print(finalText)
#
