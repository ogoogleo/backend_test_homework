"""Calculating square root from the variable programme."""


from math import sqrt


def calculate_square_root(number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float) -> float:
    """Вычисляет квадратный корень."""
    if your_number <= 0:
        return
    root = calculate_square_root(your_number)
    print('Мы вычислили квадратный корень ', end='')
    print('из введённого вами числа. Это будет: ', end='')
    print(root)


message: str = 'Добро пожаловать в самую'
message += 'лучшую программу для вычисления '
message += 'квадратного корня из заданного числа'
print(message)
print(message)
calc(25.5)
