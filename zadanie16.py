a = input()
if len(a) == 4 and len(set(a)) == 4 and not 1900 <= int(a) <= 2050:
    print("OK")
else:
    print("ERROR")