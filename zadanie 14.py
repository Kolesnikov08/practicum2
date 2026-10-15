n = int(input())
galleon = n // (17 * 29)
n = n % (17 * 29)
sickl = n // 29
knut = n % 29
if galleon > 0:
    print(galleon, "галлеонов")
if sickl > 0:
    print(sickl, "сиклей")
if knut > 0:
    print(knut, "кнатов")
