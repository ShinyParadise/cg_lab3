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


    def read_pixel(self, x_y: tuple | list) -> tuple:
        screen_coord = self.plane.plane_to_screen((x_y[0] * SIDE_LENGTH, x_y[1] * SIDE_LENGTH + SIDE_LENGTH))
        return self.screen.get_at((screen_coord[0], screen_coord[1]))[:3]
    

    def run(self, delay: float | None = None):
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

            self.clock.tick(60)
            self.update_screen()


    def run_fill(self, delay: float | None = None):
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
            color_mark = -1
            multiplier = 10
            for figure in FIGURES:
                color_mark += 1
                current_color = COLORS[color_mark]
                points = []
                p1 = Point(figure[0][0], figure[0][1], current_color)
                p2 = Point(figure[len(figure) - 1][0], figure[len(figure) - 1][1], current_color)

                p1.multiply(multiplier)
                p2.multiply(multiplier)
                points += DDA_two_points(p1, p2)

                for i in range(1, len(figure)):
                    p2 = Point(figure[i][0], figure[i][1], current_color)
                    p2.multiply(multiplier)
                    points += DDA_two_points(p1, p2)
                    p1 = p2

                for point in points:
                    cartesianPlane.draw.rect(
                        self.plane,
                        point.color,
                        (point.x * SIDE_LENGTH, point.y * SIDE_LENGTH + SIDE_LENGTH, SIDE_LENGTH, SIDE_LENGTH)
                    )

                to_fill = flood_fill(points[0], self.read_pixel, current_color, current_color)

                for point in to_fill:
                    cartesianPlane.draw.rect(
                        self.plane,
                        point.color,
                        (point.x * SIDE_LENGTH, point.y * SIDE_LENGTH + SIDE_LENGTH, SIDE_LENGTH, SIDE_LENGTH)
                    )

            self.clock.tick(60)
            self.update_screen()


    def do_delay(self, delay):
        if delay is not None:
            sleep(delay)
            self.update_screen()
