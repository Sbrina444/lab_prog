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