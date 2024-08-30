def is_prime(n):
    """Проверяет, является ли число простым."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_generator(end):
    """Генерирует простые числа до верхней границы end."""
    return (num for num in range(2, end + 1) if is_prime(num))

from inspect import isgenerator

gen = prime_generator(1)

print(isgenerator(gen))
print(list(prime_generator(10)))
print(list(prime_generator(15)))
print(list(prime_generator(29)))
print('Ok')
