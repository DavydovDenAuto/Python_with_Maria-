# def div_number(a, b):
#     res = None
#     if b != 0:
#         res = a / b
#     else:
#         print('divizion by zero')
#     return res
# x = div_number(6, 0)
# if x == None:
#     print('x == None')
# else:
#     print(int(x))
#
# #print(int(div_number(6, 0) or 0))
#
#
#
def factorial(n):
    if n < 0:
        print("n<0")
        return None
    elif n < 2:
        return 1
    else:
        return factorial(n - 1) * n


print(factorial(4))
