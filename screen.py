from time import sleep
import pygame
import cartesianPlane

from algorithms import *
from constants import *
from structs.point import *


class Screen:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Lab 3')
        self.clock = pygame.time.Clock()
        self.plane = cartesianPlane.CartesianPlane(self.screen)


    def update_screen(self):
        pygame.display.update()
    

    def draw_pixel(self, side_length, point: Point):
        cartesianPlane.draw.rect(
                self.plane, 
                point.color, 
                (point.x * side_length, point.y * side_length + side_length, side_length, side_length)
        )

    def run(self, delay: int | None = None):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

            self.plane.event_handling(event)

            self.plane.debug(
                fps=f'{self.clock.get_fps():.1f}'
            )

            # Update the plane
            self.plane.update()

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
                self.draw_pixel(SIDE_LENGTH, point)
                self.do_delay(delay)

            to_fill = flood_fill(Point(5, 5, YELLOW), points, YELLOW, RED)
            for point in to_fill:
                self.draw_pixel(SIDE_LENGTH, point)
                self.do_delay(delay) 

            self.clock.tick()
            self.update_screen()

    def do_delay(self, delay):
        if delay is not None:
            sleep(delay)
            self.update_screen()
