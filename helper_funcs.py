from structs.point import Point


def calculate_line_points(color, k: float, x: int, b: int) -> tuple[Point, Point]:
    p1 = Point(0, 0, color)   # начальная точка всегда в (0,0)

    p2x = p1.x + x
    p2y = k*x + b
    p2 = Point(p2x, p2y, color)
    return p1,p2
