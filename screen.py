from time import sleep
import pygame
import cartesianPlane

from algorithms import *
from constants import *
from structs.point import *

import time


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
                    if line:
                        # ОНО НЕ РАБОТАЕТ НОРМАЛЬНО, ПИШЕТ ЧЕРЕЗ РАЗ НУЛИ, БРЕЗЕНХЕЙМА ВООБЩЕ НЕ СЧИТАЕТ
                        # дебаг отвалился полностью, буду считать, что виновато железо
                        # count execution time in ms
                        # without display, without scale
                        k, x, b = line.split()
                        start = time.time()
                        DDA(k=int(k), x=int(x))
                        end = time.time()
                        time_measure.write(f'DDA: {(end - start) * 1000} ')
                        start = time.time()
                        brezenheim(k=int(k), x=int(x))
                        end = time.time()
                        time_measure.write(f'Brezenheim: {(end - start) * 1000}\n')

                self.plane.event_handling(event)

            self.plane.debug(
                fps=f'{self.clock.get_fps():.1f}'
            )

            # Update the plane
            self.plane.update()

            #read data for new line

            # draw here
            points_dda = DDA(k=int(k), x=int(x))
            points_brez = brezenheim(k=int(k), x=int(x))

            # БРЕЗЕНХЕЙМ СДОХ
            # find same pixel
            same_points = []
            for point in points_dda:
                if point in points_brez:
                    same_points.append(point)
                    points_dda.remove(point)
                    points_brez.remove(point)
                else:
                    point.color = BLUE

            for point in same_points:
                self.draw_pixel(SIDE_LENGTH, point)
                self.do_delay(delay)
            for point in points_dda:
                self.draw_pixel(SIDE_LENGTH, point)
                self.do_delay(delay)
            for point in points_brez:
                point.color = YELLOW
                self.draw_pixel(SIDE_LENGTH, point)
                self.do_delay(delay)

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
