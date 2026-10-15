n = int(input())
if n < 11:
    print(n - 1)
else:
    n = n - 11
    if n < 180:
        num = 10 + n // 2
        str = n % 2
        if str == 0:
            print(num // 10)
        else:
            print(num % 10)
    else:
        n = n - 180
        num = 100 + n // 3
        str = n % 3
        if str == 0:
            print(num // 100)
        elif str == 1:
            print(num // 10 % 10)
        else:
            print(num % 10)