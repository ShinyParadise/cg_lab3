import pygame
import cartesianPlane
from algorithms import *
from structs import *

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

SIDE_LENGTH = 10

FIGURES = [
    [[-4, 3], [-2, 5], [-2, 1]],
    [[-2, 5.1], [-1.6, 5.3], [-1.6, 0.7], [-2, 0.9]],
    [[-1.6, 5], [-0.6, 6.6], [0.4, 6.6], [0.4, 0.8], [0.2, 0.4], [-0.6, 0.4], [-0.8, 0.8], [-1.6, 0.8]],
    [(0.4, 5), (3, 4), (4.5, 4.5), (4.5, 1), (3, 1.5), (0.4, 0.8)],
    [(4.5, 4), (5.5, 4.5), (5.5, 1), (4.5, 1.5)],
    [(5.5, 4), (6.5, 4.5), (6.5, 1), (5.5, 1.5)],
    [(3.6, 4.2), (3.9, 4.3), (3.9, 1.2), (3.6, 1.3)],
    [(3.8, 3), (-3.5, 3.2), (-3.5, 2.8)]
]

COLORS = [
    (255, 255, 0), # yellow
    (255, 87, 36), # orange
    (255, 255, 0), # yellow
    (255, 87, 36), # orange
    (255, 255, 0), # yellow
    (252, 251, 141), # light yellow
    (252, 251, 141), # light yellow
    (0, 0, 255) # black
]

# Set up the window
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Lab 3')
clock = pygame.time.Clock()

plane = cartesianPlane.CartesianPlane(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            quit()

        plane.event_handling(event)

    plane.debug(
        fps=f'{clock.get_fps():.1f}'
    )

    # Update the plane
    plane.update()

    # draw here
    color_mark = -1
    for figure in FIGURES:
        color_mark += 1
        current_color = COLORS[color_mark]
        points = []
        p1 = Point(figure[0][0], figure[0][1], current_color)
        p2 = Point(figure[len(figure) - 1][0], figure[len(figure) - 1][1], current_color)
        points += DDA_two_points(p1, p2)
        for i in range(1, len(figure)):
            p2 = Point(figure[i][0], figure[i][1], current_color)
            points += DDA_two_points(p1, p2)
            p1 = p2

        for point in points:
            cartesianPlane.draw.rect(
                plane,
                point.color,
                (point.x * SIDE_LENGTH, point.y * SIDE_LENGTH + SIDE_LENGTH, SIDE_LENGTH, SIDE_LENGTH)
            )

#        to_fill = flood_fill(points[0], points, current_color, current_color)
#
#        for point in to_fill:
#            cartesianPlane.draw.rect(
#                plane,
#                point.color,
#                (point.x * SIDE_LENGTH, point.y * SIDE_LENGTH + SIDE_LENGTH, SIDE_LENGTH, SIDE_LENGTH)
#            )

    clock.tick()

    # Update the screen
    pygame.display.update()
