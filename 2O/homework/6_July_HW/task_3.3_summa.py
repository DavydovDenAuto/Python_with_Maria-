#Вычислите сумму первых N нечетных натуральных чисел

# method_1
def count_sum(n):
    k  = [i for i in range(n+1) if i%2==1]
    res = sum(k)
    return res
print(count_sum(10))

# method_2
