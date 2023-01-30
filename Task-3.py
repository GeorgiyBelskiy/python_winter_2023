
n = int(input())

for i in range(n):
    print(' ' * (n - i), end='')
    print(' '.join(map(str, str(11 ** i))))
# egc


# x = []
# x = input("Введите, что необходимо посчитать:")
# print((x))
# if "*" in x:
#     print(f"{x[0] * x[2]}")
# else:
#     print("NO")
