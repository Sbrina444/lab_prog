def to_str(lst):
    result, stack = [], [lst]
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(reversed(item))
        else:
            result.append(str(item))
    return ' -> '.join(result + ['None'])

print(to_str([1, [2, [3, [4, [5]]]]]))

def to_str(lst):
    if not isinstance(lst, list):
        return str(lst)
    return f"{lst[0]} -> {to_str(lst[1] if len(lst) > 1 else None)}"
print(to_str([1, [2, [3, [4, [5]]]]]))

def a(i):
    if i == 0 or i == 1:
        return 1.0
    prev2, prev1 = 1.0, 1.0
    for k in range(2, i + 1):
        prev2, prev1 = prev1, prev2 + prev1 / (2 ** (k - 1))
    return prev1
print(a(5))

def a(n):
    if n == 0 or n == 1:
        return 1
    return a(n - 2) + a(n - 1) / (2 ** (n - 1))
print(a(5))