xc = int(input("Введите xc: "))
yc = int(input("Введите yc: "))
r = int(input("Введите радиус: "))
x = int(input("Введите x: "))
y = int(input("Введите y: "))
d = (x - xc) ** 2 + (y - yc) ** 2
if d < r ** 2:
    print("Точка находится внутри окружности")
elif d == r ** 2:
    print("Точка лежит на окружности")
else:
    print("Точка находится за пределами окружности")