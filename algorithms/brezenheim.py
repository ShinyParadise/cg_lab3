from constants import RED
from helper_funcs import calculate_line_points
from structs.point import Point


def brezenheim(color: tuple = RED, k: int = 1, x: int = 30, b: int = 0) -> list[Point]:
    '''алгоритм Брезенхема - входные параметры задают уравнение прямой y=kx+b'''
    
    p1, p2 = calculate_line_points(color, k, x, b)

    return brezenheim_two_points(p1, p2)


def brezenheim_two_points(p1: Point, p2: Point) -> list[Point]:
    '''алгоритм Брезенхема - входные параметры это начальная и конечная точка'''

    points = []
    x = p1.x
    y = p1.y
    deltaX = (p2.x - p1.x) * 2
    deltaY = (p2.y - p1.y) * 2
    delta = - deltaX

    while x <= p2.x:
        points.append(Point(int(x), int(y), p1.color))
        x += 1
        delta += deltaY
        if delta >= 0:
            y += 1
            delta -= deltaX

    return points
