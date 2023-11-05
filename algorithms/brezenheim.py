from constants import RED
from helper_funcs import calculate_line_points
from structs.point import Point


def brezenheim(color: tuple = RED, k: float = 1, x: int = 30, b: int = 0) -> list[Point]:
    '''алгоритм Брезенхема - входные параметры задают уравнение прямой y=kx+b'''
    
    p1, p2 = calculate_line_points(color, k, x, b)

    return brezenheim_two_points(p1, p2)


def brezenheim_two_points(p1: Point, p2: Point) -> list[Point]:
    '''алгоритм Брезенхема - входные параметры это начальная и конечная точка'''

    points = []
    x1, y1 = p1.x, p1.y
    x2, y2 = p2.x, p2.y

    deltaY = y2 - y1
    deltaX = x1 - x2
    signY = 1
    signX = 1
    if deltaY < 0:
        signY = -1
    if deltaX < 0:
        signX = -1

    f = 0
    points.append(p1)
    if abs(deltaY) < abs(deltaX):
        while x1 != x2 or y1 != y2:
            f += deltaY * signY
            if f > 0:
                f -= deltaX * signX
                y1 += signY
            x1 -= signX
            points.append(Point(x1, y1, p1.color))
    else:
        while x1 != x2 or y1 != y2:
            f += deltaX * signX
            if f > 0:
                f -= deltaY * signY
                x1 -= signX
            y1 += signY
            points.append(Point(x1, y1, p1.color))
    return points
