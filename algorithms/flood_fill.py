# Списки соседей для каждой точки
neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def flood_fill(start, fill_color, background_color, border_color) -> list:
    # Инициализация списка точек для заполнения
    filled_points = []

    flood_fill_recursive(start, fill_color, background_color, border_color, filled_points)
    return filled_points


def flood_fill_recursive(point, fill_color, background_color, border_color, filled_points):
    # Если точка уже заполнена, выходим из рекурсии
    if point in filled_points:
        return

    # Заполняем текущую точку
    filled_points.append(point)

    # Проверяем соседей
    for neighbor in neighbors:
        new_point = (point[0] + neighbor[0], point[1] + neighbor[1])

        # Если соседняя точка не заполнена и не является границей, запускаем рекурсию
        if new_point not in filled_points and new_point not in border_color:
            flood_fill_recursive(new_point, fill_color, background_color, border_color, filled_points)
