def to_str(lst):
    if not isinstance(lst, list):
        return str(lst)
    return f"{lst[0]} -> {to_str(lst[1] if len(lst) > 1 else None)}"
print(to_str([1, [2, [3, [4, [5]]]]]))

