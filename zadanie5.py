k, a, s = map(int, input('какой счет? ').split())
if k >= a and k >= s:
    print('выиграл Кирилл')
elif a >= k and a >= s:
    print('выиграла Арина')
else:
    print('выиграл Серега')