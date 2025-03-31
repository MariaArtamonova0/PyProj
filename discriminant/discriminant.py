import math

def solve_quadratic(a, b, c):
    if a == 0:
        print("Это не квадратное уравнение.")
        return

    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"Два корня: x1 = {x1}, x2 = {x2}")
    elif discriminant == 0:
        x = -b / (2 * a)
        print(f"Один корень: x = {x}")
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
        print(f"Комплексные корни: x1 = {real_part} + {imaginary_part}i, x2 = {real_part} - {imaginary_part}i")


# Пример использования:
a, b, c = map(float, input("Введите коэффициенты a, b, c через пробел: ").split())
solve_quadratic(a, b, c)