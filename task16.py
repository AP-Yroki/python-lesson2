n = int(input("Введите число: "))
m = int(input("Введите число: "))
x = int(input("Введите число: "))
y = int(input("Введите число: "))

if n > m:
    n, m = m, n
if x >= n / 2:
    x = n - x
if y >= m / 2:
    y = m - y
# print(min(x, y))
if x < y:
    print(x)
else:
    print(y)
