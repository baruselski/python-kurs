# Laboratorium 3 Zadanie 3 Podpunkt 'b'

import timeit
from functools import lru_cache

# Recursive fibonacci function
def fibonacci_recursive(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        fib_sequence = fibonacci_recursive(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

# Dekorator lru_cache
@lru_cache
def fibonacci_recursive_cached(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        fib_sequence = fibonacci_recursive_cached(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

# Pomiar czasu dla funkcji rekurencyjnej
start_time = timeit.default_timer()
result_recursive = fibonacci_recursive(30)
end_time = timeit.default_timer()
print(f"Czas dla funkcji rekurencyjnej: {end_time - start_time} sekundy")
print(f"Wynik: {result_recursive}")

# Pomiar czasu dla funkcji rekurencyjnej z użyciem dekoratora lru_cache
start_time_cached = timeit.default_timer()
result_cached = fibonacci_recursive_cached(30)
end_time_cached = timeit.default_timer()
print(f"Czas dla funkcji rekurencyjnej z dekoratorem lru_cache: {end_time_cached - start_time_cached} sekundy")
print(f"Wynik: {result_cached}")
