import os
import ast


def log_result(file_path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Utwórz unikalną nazwę pliku na podstawie parametrów funkcji
            file_name = file_path + '_' + '_'.join(map(str, args)) + '_'.join(
                f'{key}_{value}' for key, value in kwargs.items()) + '.txt'

            # Sprawdź, czy plik już istnieje
            if os.path.exists(file_name):
                # Wczytaj dane z pliku tekstowego
                with open(file_name, 'r') as file:
                    result_str = file.read()
                    result = ast.literal_eval(result_str)
            else:
                # Oblicz wynik funkcji
                result = func(*args, **kwargs)

                # Zapisz wynik do pliku tekstowego
                with open(file_name, 'w') as file:
                    # Zapisz łańcuchową reprezentację wyniku
                    file.write(str(result))

            return result

        return wrapper

    return decorator


@log_result(r'C:\Users\Bartek\PycharmProjects\Python1\python-kurs\result')
def fibonacci_recursive(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        fib_sequence = fibonacci_recursive(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence


# Wywołaj funkcję z dekoratorem
result = fibonacci_recursive(10)
print(f"Wynik: {result}")

# Ponowne wywołanie funkcji z dekoratorem - wynik zostanie wczytany z pliku, a nie obliczony ponownie
result_log = fibonacci_recursive(10)
print(f"Wynik (z pliku): {result_log}")
