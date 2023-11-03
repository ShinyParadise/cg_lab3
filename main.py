import pygame
import cartesianPlane
import algorithms as algos

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
    algos.DDA(0, 0, 10, 10)

    clock.tick()

    # Update the screen
    pygame.display.update()
