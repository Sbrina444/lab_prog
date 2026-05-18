#Задача 1
from itertools import product
letters = ['Н', 'А', 'С', 'Т', 'Я']
vowels = ['А', 'Я']
count = 0
for code in product(letters, repeat=6):
    if code.count('А') <= 1 and code.count('Я') <= 1:
        count += 1
print('Ответ 1:',count)

#Задача 2
value = 16**18 * 4**10 - 46 - 16
def to_base4(n):
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append(str(n % 4))
        n //= 4
    return ''.join(reversed(digits))
base4_repr = to_base4(value)
count_of_3 = base4_repr.count('3')
print("Ответ 2:",count_of_3)

#Задача 3
def find_min_max_divisors(n):
    divisors = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:  # добавляем парный делитель, если он не совпадает
                divisors.append(n // i)
    if not divisors:
        return 0
    return min(divisors) + max(divisors)
def main():
    start = 452022
    count = 0
    results = []
    while count < 5:
        M = find_min_max_divisors(start)
        if M % 7 == 3:
            results.append((start, M))
            count += 1
        start += 1
    print("Ответ 3:")
    for num, M in results:
        print(num, M)

if __name__ == "__main__":
    main()
