def sum_of_divisors(n):
    """
    Вычисляет сумму собственных делителей числа n.

    Args:
        n: Целое число.

    Returns:
        Сумма собственных делителей числа n.
    """
    if n <= 1:
        return 0
    total = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:  # Чтобы не добавлять делитель дважды (например, для 16 = 4*4)
                total += n // i
    return total


def is_perfect_number(n):
    """
    Проверяет, является ли число n совершенным.

    Args:
        n: Целое число.

    Returns:
        True, если число n совершенное, иначе False.
    """
    return n > 1 and sum_of_divisors(n) == n


def find_perfect_numbers(limit):
    """
    Находит все совершенные числа в заданном диапазоне.

    Args:
        limit: Верхняя граница диапазона (включительно).

    Returns:
        Список всех совершенных чисел в диапазоне от 1 до limit.
    """
    perfect_numbers = []
    for i in range(2, limit + 1):
        if is_perfect_number(i):
            perfect_numbers.append(i)
    return perfect_numbers


if __name__ == '__main__':
    limit = 10000
    perfect_nums = find_perfect_numbers(limit)
    print(f"Совершенные числа до {limit}: {perfect_nums}")