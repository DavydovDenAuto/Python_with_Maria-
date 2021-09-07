# Выведите таблицу умножения Пифагора, чтобы единицы были под единицами
# 1
for i in range(1, 11):
    for j in range(i, i * 11, i):
        print(j, end='\t')
    print()

print()
print()

# 2
s1 = 10
for i in range(1, s1 + 1):
    print(*range(i, i * (s1 + 1), i), sep='\t')
