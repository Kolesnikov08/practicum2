n = int(input("Введите число: "))
if n  >= 11 and n <= 14:
    print(n, "попугаев")
elif n % 10 == 1:
    print(n, "попугай")
elif n % 10 >= 2 and n % 10 <= 4:
    print(n, "попугая")
else:
    print(n, "попугаев")