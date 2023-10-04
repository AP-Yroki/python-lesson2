# n = int(input("Введите число: "))
# m = int(input("Введите число: "))
# k = int(input("Введите число: "))
#
# if k < n * m and ((k % n == 0) or (k % m == 0)):
#     print("YES")
# else:
#     print("NO")


n = int(input("Введите число: "))
m = int(input("Введите число: "))
k = int(input("Введите число: "))

sqrt = n * m
result = sqrt / 2
if result == k:
    print("YES")
else:
    print("NO")


# Оба скрипта рабочие, и выполняют одну и ту же функцию, не мог определиться какую именно оставить, поэтому закинул сразу 2