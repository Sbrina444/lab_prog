def a(n):
    if n == 0 or n == 1:
        return 1
    return a(n - 2) + a(n - 1) / (2 ** (n - 1))
print(a(5))