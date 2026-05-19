def a(i):
    if i == 0 or i == 1:
        return 1.0
    prev2, prev1 = 1.0, 1.0
    for k in range(2, i + 1):
        prev2, prev1 = prev1, prev2 + prev1 / (2 ** (k - 1))
    return prev1
print(a(5))

