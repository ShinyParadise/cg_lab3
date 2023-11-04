from structs.point import Point

# Списки соседей для каждой точки
neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def flood_fill(start_point: Point, fill_color, border_color) -> list:
    # Инициализация списка точек для заполнения
    filled_points = []

    flood_fill_recursive(start_point, border_color, filled_points)
    return filled_points


def flood_fill_recursive(point: Point, fill_color, border_color, filled_points):
    # Если точка уже заполнена, выходим из рекурсии
    if point in filled_points:
        return

    # Заполняем текущую точку
    filled_points.append(point)

    # Проверяем соседей
    for neighbor in neighbors:
        new_point = Point(point.x + neighbor[0], point.y + neighbor[1], fill_color)

        # Если соседняя точка не заполнена и не является границей, запускаем рекурсию
        if new_point not in filled_points and new_point.color != border_color:
            flood_fill_recursive(new_point, fill_color, border_color, filled_points)
