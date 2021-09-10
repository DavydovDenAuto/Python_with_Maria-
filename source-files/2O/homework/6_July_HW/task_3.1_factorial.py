# Вычислите факториал введенного числа с помощью цикла каждого вида
# 5f  = 1*2*3*4*5 n*(n+1)
# def count_faktorial():
#     num = int(input('Enter number: '))
#     print(f'factorial of {num} is:')
#     k = 1
#     while num > 0:
#         k = k * num
#         num -= 1
#     return k
#
#
# print(count_faktorial())

# print(math.factorial(4))


def count_factorial(num):
    res = 1
    for i in range(1, num+1):
        res = res*i
    return res


print(count_factorial(5))
