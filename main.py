import pygame
import cartesianPlane
from algorithms import *
from structs import *

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

SIDE_LENGTH = 10

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
    p1 = Point(0, 0, RED)
    p2 = Point(0, 10, RED)
    p3 = Point(10, 0, RED)
    p4 = Point(10, 10, RED)

    points = DDA(p1, p2)
    points += DDA(p2, p4)
    points += DDA(p4, p3)
    points += DDA(p3, p1)

    for point in points:
        cartesianPlane.draw.rect(
            plane, 
            point.color, 
            (point.x * SIDE_LENGTH, point.y * SIDE_LENGTH + SIDE_LENGTH, SIDE_LENGTH, SIDE_LENGTH)
        )

    to_fill = flood_fill(Point(5, 5, YELLOW), points, YELLOW, RED)
    for point in to_fill:
        cartesianPlane.draw.rect(
            plane, 
            point.color, 
            (point.x * SIDE_LENGTH, point.y * SIDE_LENGTH + SIDE_LENGTH, SIDE_LENGTH, SIDE_LENGTH)
        )

    clock.tick()

    # Update the screen
    pygame.display.update()
