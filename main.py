import pygame
import cartesianPlane
from algorithms import *
from structs import *

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Set up the window
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Cartesian Plane')
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
    p2 = Point(10, 10, RED)
    points = DDA(p1, p2)
    print(points)

    clock.tick()

    # Update the screen
    pygame.display.update()
