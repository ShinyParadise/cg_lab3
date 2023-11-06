from constants import RED
from helper_funcs import calculate_line_points, sign
from structs.point import Point


def DDA(color: tuple = RED, k: float = 1, x: int = 30, b: int = 0) -> list[Point]:
    '''алгоритм ЦДА - входные параметры задают уравнение прямой y=kx+b'''

    p1, p2 = calculate_line_points(color, k, x, b)

    return DDA_two_points(p1, p2)


def DDA_two_points(p1: Point, p2: Point) -> list[Point]:
    '''алгоритм ЦДА - входные параметры это начальная и конечная точка'''
    points = []
    if abs(p2.x - p1.x) >= abs(p2.y - p1.y):
        length = abs(p2.x - p1.x)
    else:
        length = abs(p2.y - p1.y)

    dx = (p2.x - p1.x) / length
    dy = (p2.y - p1.y) / length

    x = p1.x + 0.5 * sign(dx)
    y = p1.y + 0.5 * sign(dy)

    i = 1
    while i <= length:
        points.append(Point(int(x), int(y), p1.color))
        x = x + dx
        y = y + dy
        i += 1

    return points
