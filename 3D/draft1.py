

with open('D:\\Python\\python_1M_2O_3D\\2O\\lessons\\hello1.txt','a') as myfile:
    myfile.write('\n\t Hi Den')
    print("\n string 3", file=myfile)

with open('D:\\Python\\python_1M_2O_3D\\2O\\lessons\\hello1.txt','r') as myfile:
    for line in myfile:
        print(line, end='')