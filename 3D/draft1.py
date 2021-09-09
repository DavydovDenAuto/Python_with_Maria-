

# with open('D:\\Python\\python_1M_2O_3D\\2O\\lessons\\hello1.txt','a') as myfile:
#     myfile.write('\n\t Hi Den')
#     print("\n string 3", file=myfile)
#
# with open('D:\\Python\\python_1M_2O_3D\\2O\\lessons\\hello1.txt','r') as myfile:
#     for line in myfile:
#         print(line, end='')

'''
Файловый ввод и вывод. Если не указано другое,
В простом варианте считать, что слова разделены одним пробелом, предложения - точками.
В сложном варианте учесть разные знаки препинания и несколько пробелов подряд. 
Текст ввести в файл TEXT.TXT. Результаты работы программы записать в файл REZULT.TXT.
8.1. Поменяйте в каждом предложении текста первое слово с последним.
'''
s = "Hello.I'm so happy to see you."
with open('text.txt','w') as myfile:
    myfile.write(s)

with open('text.txt','r') as myfile:
    #lst = s.split() ["Hello.I'm", 'so', 'happy', 'to', 'see', 'you.']
    lst = s.replace('.', '').split() #["HelloI'm", 'so', 'happy', 'to', 'see', 'you']
    print(lst)
    lst[0],lst[-1]=lst[-1],lst[0]
    print(lst)

