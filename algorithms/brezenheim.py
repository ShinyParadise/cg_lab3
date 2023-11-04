from structs.point import Point

def brezenheim(p1: Point, p2: Point) -> list:

    points = []
    x = p1.x
    y = p1.y
    deltaX = (p2.x - p1.x) * 2
    deltaY = (p2.y - p1.y) * 2
    delta = - deltaX

    while x <= p2.x:
        points.append((int(x), int(y)))
        x += 1
        delta += deltaY
        if delta >= 0:
            y += 1
            delta -= deltaX

    return points
