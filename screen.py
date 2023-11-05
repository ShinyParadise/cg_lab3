from time import sleep
import pygame
import cartesianPlane

from algorithms import *
from constants import *
from structs.point import *

from timeit import default_timer as timer
from datetime import timedelta


class Screen:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Lab 3')
        self.clock = pygame.time.Clock()
        self.plane = cartesianPlane.CartesianPlane(self.screen)
        self.file = "lines_data.txt"
        self.time_measure = "time.txt"


    def update_screen(self):
        pygame.display.update()
    

    def draw_pixel(self, side_length, point: Point):
        cartesianPlane.draw.rect(
                self.plane, 
                point.color, 
                (point.x * side_length, point.y * side_length + side_length, side_length, side_length)
        )

    def run(self, delay: int | None = None):
        difference_DDA = 0
        difference_brez = 0
        point_data = open(self.file, 'r')
        time_measure = open(self.time_measure, 'w')
        k, x, b = point_data.readline().split()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    point_data.close()
                    time_measure.close()
                    quit()
                if event.type == pygame.KEYDOWN:
                    line = point_data.readline()
                    time_measure.write(f' {difference_DDA} {difference_brez}\n')
                    if line:
                        k, x, b = line.split()
                        start = timer()
                        points_q = len(DDA(k=float(k), x=int(x)))
                        end = timer()
                        time_measure.write(f'DDA: {timedelta(seconds=end-start)}, points number: {points_q} ')
                        start = timer()
                        points_q = len(brezenheim(k=float(k), x=int(x)))
                        end = timer()
                        time_measure.write(f'Brezenheim: {timedelta(seconds=end-start)}, points number: {points_q}')

                self.plane.event_handling(event)

            self.plane.debug(
                fps=f'{self.clock.get_fps():.1f}'
            )

            # Update the plane
            self.plane.update()

            # draw here
            points_dda = DDA(k=float(k), x=int(x))
            points_brez = brezenheim(k=float(k), x=int(x))

            # find same pixel
            difference_DDA = 0
            difference_brez = 0
            for point in points_dda:
                if points_brez.count(point):

                    points_brez.remove(point)
                else:
                    point.color = BLUE
                    difference_DDA += 1

            for point in points_dda:
                self.draw_pixel(SIDE_LENGTH, point)
                self.do_delay(delay)

            for point in points_brez:
                point.color = YELLOW
                self.draw_pixel(SIDE_LENGTH, point)
                self.do_delay(delay)
                difference_brez += 1

            # to_fill = flood_fill(Point(5, 5, YELLOW), points_dda, YELLOW, RED)
            # for point in to_fill:
            #     self.draw_pixel(SIDE_LENGTH, point)
            #     self.do_delay(delay) 

            self.clock.tick(60)
            self.update_screen()

    def do_delay(self, delay):
        if delay is not None:
            sleep(delay)
            self.update_screen()
