a = int(input("введите число "))
n4 = a % 10
n3 = (a // 10) % 10
n2 = (a // 100) % 10
n1 = a // 1000
if n1 == n4 and n2 == n3:
    print("настоящее")
else:
    print("кривое")