n, k, m = map(int, input().split())
a = abs(k - m)
print(min(a, n - a) - 1)