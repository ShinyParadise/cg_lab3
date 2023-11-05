from structs.point import Point
from typing import Callable


def modified_stack_fill(start_point: Point, get_pixel: Callable[[tuple], tuple], fill_color, border_color):
    # Инициализация списка точек для заполнения
    filled_points = []

    modified_stack(start_point, get_pixel, fill_color, border_color, filled_points)
    return filled_points


def modified_stack(start_point: Point, get_pixel: Callable[[tuple], tuple], fill_color, border_color, filled_points):
    stack_points = [start_point]

    while len(stack_points):
        find_upper = False
        find_lower = False

        work_point = stack_points.pop()
        float_point = Point(work_point.x + 1, work_point.y, fill_color)
        filled_points.append(work_point)
        # to the right

        while float_point not in filled_points and not check_for_border(float_point, get_pixel, border_color):
            filled_points.append(float_point)
            if not find_upper and not \
                    check_for_border(Point(float_point.x, float_point.y + 1, border_color),
                                     get_pixel, border_color) and\
                    Point(float_point.x, float_point.y + 1, fill_color) not in filled_points:
                find_upper = True
                stack_points.append(Point(float_point.x, float_point.y + 1, border_color))
            if not find_lower and not \
                    check_for_border(Point(float_point.x, float_point.y - 1, border_color),
                                     get_pixel, border_color) and\
                    Point(float_point.x, float_point.y - 1, fill_color) not in filled_points:
                find_lower = True
                stack_points.append(Point(float_point.x, float_point.y - 1, fill_color))
            float_point.x += 1

        # to the left
        float_point = Point(work_point.x - 1, work_point.y, fill_color)
        while float_point not in filled_points and not check_for_border(float_point, get_pixel, border_color):
            if not find_upper and not \
                    check_for_border(Point(float_point.x, float_point.y + 1, border_color),
                                     get_pixel, border_color) and\
                    Point(float_point.x, float_point.y + 1, fill_color) not in filled_points:
                find_upper = True
                stack_points.append(Point(float_point.x, float_point.y + 1, border_color))
            if not find_lower and not \
                    check_for_border(Point(float_point.x, float_point.y - 1, border_color),
                                     get_pixel, border_color) and\
                    Point(float_point.x, float_point.y - 1, fill_color) not in filled_points:
                find_lower = True
                stack_points.append(Point(float_point.x, float_point.y - 1, fill_color))
            float_point.x -= 1

    return filled_points


def check_for_border(point: Point, get_pixel: Callable[[tuple], tuple], border_color: tuple):
    actual_pixel_color = get_pixel((point.x, point.y))

    return border_color == actual_pixel_color
