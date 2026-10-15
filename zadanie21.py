s1, s2 = input().split()
x1 = ord(s1[0]) - 97
y1 = int(s1[1])
x2 = ord(s2[0]) - 97
y2 = int(s2[1])
if (abs(x1 - x2) == 1 and abs(y1 - y2) == 2) or (abs(x1 - x2) == 2 and abs(y1 - y2) == 1):
    print("да")
else:
    print("нет")