n, k, m = map(int, input().split())
ch = n * 2
if ch % k == 0:
    poe = ch // k
else:
    poe = ch // k + 1
t = poe * m
print(t)