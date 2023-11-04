from structs.point import Point

def brezenheim(p1: Point, p2: Point) -> list[Point]:

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
