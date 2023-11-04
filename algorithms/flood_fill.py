from structs.point import Point

# Списки соседей для каждой точки
neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def flood_fill(start_point: Point, border_points: list[Point], fill_color, border_color) -> list[Point]:
    # Инициализация списка точек для заполнения
    filled_points = []

    flood_fill_recursive(start_point, border_points, fill_color, border_color, filled_points)
    return filled_points


def flood_fill_recursive(point: Point, border_points: list[Point], fill_color, border_color, filled_points):
    # Если точка уже заполнена, выходим из рекурсии
    if point in filled_points:
        return

    # Заполняем текущую точку
    filled_points.append(point)

    # Проверяем соседей
    for neighbor in neighbors:
        new_point = Point(point.x + neighbor[0], point.y + neighbor[1], fill_color)

        # Если соседняя точка не заполнена и не является границей, запускаем рекурсию
        if new_point not in filled_points and not check_for_border(new_point, border_points):
            flood_fill_recursive(new_point, border_points, fill_color, border_color, filled_points)


def check_for_border(point: Point, border_points: list[Point]):
    for bp in border_points:
        if bp.x == point.x and bp.y == point.y:
            return True

    return False    
