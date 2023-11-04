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
    x1, y1 = p1.x, p1.y
    x2, y2 = p2.x, p2.y
    yChange = 1

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    if y1 > y2:
        yChange = -1

    deltaX = (x2 - x1) * 2
    deltaY = yChange * (y2 - y1) * 2
    delta = - deltaX

    while x1 <= x2:
        points.append(Point(int(x1), int(y1), p1.color))
        x1 += 1
        delta += deltaY
        if delta >= 0:
            y1 += yChange
            delta -= deltaX

    return points
