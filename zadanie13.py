ves = float(input("Введите вес в кг: "))
rost = float(input("Введите рост в метрах: "))
bmi = ves / rost ** 2
if bmi < 16:
    print("Выраженный дефицит массы тела")
elif bmi < 18.5:
    print("Недостаточная масса тела")
elif bmi < 25:
    print("Норма")
elif bmi < 30:
    print("Избыточная масса тела")
elif bmi < 35:
    print("Ожирение первой степени")
elif bmi < 40:
    print("Ожирение второй степени")
else:
    print("Ожирение третьей степени")