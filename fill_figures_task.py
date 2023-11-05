import pygame
import cartesianPlane
from algorithms import *
from structs import *
import constants as co

from timeit import default_timer as timer
from datetime import timedelta


def read_pixel(x_y: tuple | list) -> tuple:
    screen_coord = plane.plane_to_screen((x_y[0] * co.SIDE_LENGTH, x_y[1] * co.SIDE_LENGTH + co.SIDE_LENGTH))
    return screen.get_at((screen_coord[0], screen_coord[1]))[:3]


def draw_borders(x1, y1, x2, y2, x3, y3, x4, y4):
    p1 = Point(x1, y1, co.RED)
    p2 = Point(x2, y2, co.RED)
    p3 = Point(x3, y3, co.RED)
    p4 = Point(x4, y4, co.RED)
    dots = DDA_two_points(p1, p2)
    dots += DDA_two_points(p2, p3)
    dots += DDA_two_points(p3, p4)
    dots += DDA_two_points(p4, p1)
    for dot in dots:
        cartesianPlane.draw.rect(
            plane,
            dot.color,
            (dot.x * co.SIDE_LENGTH, dot.y * co.SIDE_LENGTH + co.SIDE_LENGTH, co.SIDE_LENGTH, co.SIDE_LENGTH)
        )


# Set up the window
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Lab 3')
clock = pygame.time.Clock()

plane = cartesianPlane.CartesianPlane(screen)
fig_num = -1
fig_count = len(co.SQARES) - 1
result_file = open('square.txt', 'w')
x1, y1, x2, y2, x3, y3, x4, y4 = 0, 0, 0, 10, 10, 10, 10, 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            result_file.close()
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN and fig_num < fig_count:
            fig_num += 1
            x1, y1, x2, y2, x3, y3, x4, y4 = [e for e in co.SQARES[fig_num]]
            draw_borders(x1, y1, x2, y2, x3, y3, x4, y4)
            start = timer()
            points_q = len(flood_fill(Point(2, 2, co.YELLOW), read_pixel, co.YELLOW, co.RED))
            end = timer()
            result_file.write(f'Flood fill: {timedelta(seconds=end - start)}, points number: {points_q} ')
            start = timer()
            points_q = len(flood_fill(Point(2, 2, co.YELLOW), read_pixel, co.YELLOW, co.RED))
            end = timer()
            result_file.write(f'Modified stack fill: {timedelta(seconds=end - start)}, points number: {points_q}\n')

        plane.event_handling(event)

    plane.debug(
        fps=f'{clock.get_fps():.1f}'
    )

    # Update the plane
    plane.update()

    # draw here
    draw_borders(x1, y1, x2, y2, x3, y3, x4, y4)
    to_fill = flood_fill(Point(5, 5, co.YELLOW), read_pixel, co.YELLOW, co.RED)
    for point in to_fill:
        cartesianPlane.draw.rect(
            plane,
            point.color,
            (point.x * co.SIDE_LENGTH, point.y * co.SIDE_LENGTH + co.SIDE_LENGTH, co.SIDE_LENGTH, co.SIDE_LENGTH)
        )

    clock.tick()

    # Update the screen
    pygame.display.update()
