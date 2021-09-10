"""
Подсчитано что легковый авто при среднегодовом пробеге 15тыс.км выдыхает 250кг углекислого газа,93 кг углеводорода
 и 27 кг оксида азота. Составьте прогу для расчета кол-ва выделяемых веществ в год при к-количестве авто в городе
"""
import colorama
from colorama import Fore, Back, Style

colorama.init()


def count_emission(mileage=15000, CO2=250, CH=93, N2O3=27):
    k = int(input('Input cars amount:'))
    emission = k * (CO2 + CH + N2O3)
    return k, emission


k, emission = count_emission()
print(Fore.RED + f'При {k} авто в городе', Fore.BLUE + f'кол-во выбросов будет равно {emission}')
colorama.deinit()
"""
Главный потребитель воды - сельское хоз-во. Оно использует 70% всей воды используемой человеком.
Чтобы вырастить 1 тонну пшеницы необходимо 1500тонн воды, а 1 тонну риса 7000т воды.
Составьте программу для вычисления  кол-ва воды нужного чтобы вырастить пшеницу на поле площадь которого m гектар
если урожайность пшеницы 2,2т
"""


def count_water(productivity=2.2, consumption=1500):
    m = int(input('Enter field square: '))
    required_water = m * productivity * consumption
    return m, required_water


m, required_water = count_water()
print(f'При площади поля {m} гектар, необходимо {round(required_water, 2)} тонн воды')

"""
Вычислить, сколько кубических метров воздуха очистит от автомобильных выхлопных газов n каштанов посаженных вдоль дороги 
если одно дерево очищает зону длиной 100метров, шириной 20м, высотой 10м без вреда для себя
"""


def count_freshAir(length=100, height=10, width=20):
    n = int(input('Enter amount of chestnut: '))
    chestnut_clean = n * (length * height * width)
    return n, chestnut_clean


n, chestnut_clean = count_freshAir()
print(f'При количестве каштанов равному {n} , будет очищено {chestnut_clean} кубометров воздуха')

"""
Одно дерево освежает воздух как 10 кондиционеров. Сколько кондиционеров заменят n деревьев
"""
