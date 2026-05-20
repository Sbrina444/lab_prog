def limit_calls(max_calls):
    def decorator(func):
        count = 0

        def wrapper(value):
            nonlocal count
            if count >= max_calls:
                print("Стоп: слишком много вызовов")
                return None
            count += 1
            return func(value)

        return wrapper

    return decorator

def unique_values():
    seen = []

    @limit_calls(5)
    def inner(value):
        if value not in seen:
            seen.append(value)
            return value

        return None
    return inner

f = unique_values()

data = [1, 2, 2, 3, 1, 4, 5]

for x in data:
    result = f(x)

    if result is not None:
        print(result)