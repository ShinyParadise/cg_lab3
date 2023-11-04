from structs.point import Point


def DDA(p1: Point, p2: Point) -> list[Point]:
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


def sign(x):
    if (x > 0):
        return 1
    else:
        return -1
