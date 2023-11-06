from constants import RED
from helper_funcs import calculate_line_points, sign
from structs.point import Point


def brezenheim(color: tuple = RED, k: float = 1, x: int = 30, b: int = 0) -> list[Point]:
    '''алгоритм Брезенхема - входные параметры задают уравнение прямой y=kx+b'''
    
    p1, p2 = calculate_line_points(color, k, x, b)

    return brezenheim_two_points(p1, p2)


def brezenheim_two_points(p1: Point, p2: Point) -> list[Point]:
    '''алгоритм Брезенхема - входные параметры это начальная и конечная точка'''

    points = []
    x1, y1, x2, y2 = int(p1.x), int(p1.y), int(p2.x), int(p2.y)

    x = x1
    y = y1
    dx = abs(x2-x1)
    dy = abs(y2-y1)

    s1 = sign(x2-x1)
    s2 = sign(y2-y1)

    change = False
    if dy > dx:
        dx, dy = dy, dx
        change = True
    
    e = 2 * dy - dx

    i = 1
    while i != dx:
        while e >= 0:
            if change:
                x += s1
            else:
                y += s2
            e -= 2 * dx

        if change:
            y += s2
        else:
            x += s1

        e += 2 * dy
        i += 1
        points.append(Point(x, y, p1.color))
    
    return points
