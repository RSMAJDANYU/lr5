import time
import math
import matplotlib.pyplot as plt


def recursive_F(n):
    """Вычисление функции F(n) рекурсивным методом"""
    if n == 1:
        return 1
    if n % 2 == 0:
        return (-1) ** n * (recursive_F(n - 1) / math.factorial(2 * n)) - (n + math.sin(n))
    else:
        return math.factorial(n)


def iterative_F(n):
    """Вычисление функции F(n) итерационным методом"""
    if n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        if i % 2 == 0:
            result = (-1) ** i * (result / math.factorial(2 * i)) - (i + math.sin(i))
        else:
            result = math.factorial(i)
    return result


def measure_performance(max_n=15):
    """Сравнение производительности методов"""
    n_values = list(range(1, max_n + 1))
    rec_times = []
    iter_times = []

    for n in n_values:
        # Замер рекурсивного метода
        start = time.perf_counter()
        recursive_F(n)
        rec_times.append(time.perf_counter() - start)

        # Замер итерационного метода
        start = time.perf_counter()
        iterative_F(n)
        iter_times.append(time.perf_counter() - start)

    return n_values, rec_times, iter_times


def print_results(n_values, rec_times, iter_times):
    """Вывод результатов в табличном виде"""
    print("\nСравнение времени выполнения (в секундах):")
    print("n\tРекурсия\tИтерация")
    print("-" * 30)
    for n, rt, it in zip(n_values, rec_times, iter_times):
        print(f"{n}\t{rt:.6f}\t{it:.6f}")


def plot_results(n_values, rec_times, iter_times):
    """Визуализация результатов"""
    plt.figure(figsize=(10, 5))
    plt.plot(n_values, rec_times, 'o-', label='Рекурсивный метод')
    plt.plot(n_values, iter_times, 's-', label='Итерационный метод')
    plt.xlabel('Значение n')
    plt.ylabel('Время выполнения (с)')
    plt.title('Сравнение производительности методов вычисления')
    plt.legend()
    plt.grid(True)
    plt.show()


def find_threshold(rec_times, iter_times, n_values):
    """Определение границы применимости рекурсии"""
    for n, rt, it in zip(n_values, rec_times, iter_times):
        if rt > it * 3:  # Рекурсия становится в 3 раза медленнее
            return n
    return None


# Основная часть программы
if __name__ == "__main__":
    try:
        max_n = int(input("Введите максимальное значение n для исследования (рекомендуется 15-20): "))
        if max_n < 1:
            raise ValueError
    except ValueError:
        print("Ошибка: введите целое число больше 0")
        exit()

    n_vals, rec_t, iter_t = measure_performance(max_n)

    print_results(n_vals, rec_t, iter_t)
    plot_results(n_vals, rec_t, iter_t)

    threshold = find_threshold(rec_t, iter_t, n_vals)
    if threshold:
        print(f"\nРекурсивный метод становится неэффективным при n >= {threshold}")
    else:
        print("\nВ исследованном диапазоне рекурсивный метод остается конкурентоспособным")