from ast import If
from pickle import NONE
from random import randint
import sys
from time import time
from tkinter import CENTER, font
from tracemalloc import start
from turtle import color
import pygame
from sys import exit
import time
import math


def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score


def car_movement(car_list):
    if car_list:
        for car_rect in car_list:
            if car_rect.x > 500:
                screen.blit(car, car_rect)
            car_list = [car for car in car_list if car.x > 1100]

        return car_list
    else:
        return []


def display_score():

    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    infoAttempt = game_font.render(
        f'Attempts: {nrOfAttempts}', False, (65, 65, 65))
    infoAttempt_rect = infoAttempt.get_rect(center=(180, 380))
    info_surfQ = game_font.render(
        f"s- Stop", False, (70, 70, 70))
    info_rectQ = info_surfQ.get_rect(center=(720, 120))
    score_surf = game_font.render(
        f'Score: {current_time} s', False, (60, 60, 60))
    score_rect = score_surf.get_rect(center=(180, 120))
    screen.blit(score_surf, score_rect)
    screen.blit(info_surfQ, info_rectQ)
    screen.blit(infoAttempt, infoAttempt_rect)
    if current_time == 0:
        current_time = 1
        return current_time
    else:
        return current_time


def blitRotateCenter(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(
        center=image.get_rect(topleft=topleft).center)

    surf.blit(rotated_image, new_rect)


# start
pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Traffic Light System")

PATH = [(175, 119), (110, 70), (56, 133), (70, 481), (318, 731), (404, 680), (418, 521), (507, 475), (600, 551), (613, 715), (736, 713),
        (734, 399), (611, 357), (409, 343), (433, 257), (697, 258), (738, 123), (581, 71), (303, 78), (275, 377), (176, 388), (178, 260)]

clock = pygame.time.Clock()
game_active = False
start_time = 0
score = 0
game_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_font1 = pygame.font.Font('font/Pixeltype.ttf', 30)
high_score = 0
nrOfAttempts = 0

# intro
game_name = game_font.render('Traffic control simulation', False, (65, 65, 65))
game_name_rect = game_name.get_rect(center=(480, 200))
game_message = game_font.render('Press SPACE to start', False, (255, 255, 255))
game_message_rect = game_message.get_rect(center=(480, 280))


# roads
roadFromLeft = pygame.Surface([1000, 100])
roadFromLeft.fill((128, 128, 118))
roadFromLeft_rect = roadFromLeft.get_rect(topleft=(0, 200))

roadFromTop = pygame.Surface([100, 500])
roadFromTop.fill((128, 128, 118))
roadFromTop_rect = roadFromTop.get_rect(topleft=(450, 0))

roadOutlineHorizontal = pygame.Surface([450, 10])
roadOutlineHorizontal.fill((160, 154, 154))
roadOutlineHorizontal_rect = roadOutlineHorizontal.get_rect(topleft=(0, 190))

roadOutlineVertical = pygame.Surface([10, 200])
roadOutlineVertical.fill((160, 154, 154))
roadOutlineVertical_rect = roadOutlineVertical.get_rect(topleft=(440, 0))

# cars from left
car = pygame.image.load('graphics/car.png').convert_alpha()
car = pygame.transform.scale(car, (15, 12))
car_rect = car.get_rect(topleft=(10, 275))
sides = ['top', 'bottom', 'left', 'right']

car1 = pygame.image.load('graphics/car.png').convert_alpha()
car1 = pygame.transform.scale(car1, (15, 12))
car_rect1 = car1.get_rect(topleft=(10, 255))


# cars from right
car2 = pygame.image.load('graphics/carLeft.png').convert_alpha()
car2 = pygame.transform.scale(car2, (15, 12))
car_rect2 = car2.get_rect(topleft=(980, 205))


car3 = pygame.image.load('graphics/carLeft.png').convert_alpha()
car3 = pygame.transform.scale(car3, (15, 12))
car_rect3 = car3.get_rect(topleft=(980, 230))

# cars from top 4 && 5
car4 = pygame.image.load('graphics/carT.png').convert_alpha()
car4 = pygame.transform.scale(car4, (15, 12))
car_rect4 = car4.get_rect(topleft=(450, 10))


car5 = pygame.image.load('graphics/carD.png').convert_alpha()
car5 = pygame.transform.scale(car5, (15, 12))
car_rect5 = car5.get_rect(topleft=(530, 480))


cars = [car, car1, car2, car3, car4, car5]
# traffic light
yellow = (249, 215, 30)
red = (255, 0, 0)
green = (0, 255, 0)

light_on = 0


light = pygame.Surface([10, 10])
light.fill((0, 0, 0))
light_rect = light.get_rect(topleft=(440, 269))

red_light = pygame.Surface([7, 7])
red_light.fill(red)
red_light_rect = light.get_rect(topleft=(440, 269))


green_light = pygame.Surface([7, 7])
green_light.fill(green)
green_light_rect = light.get_rect(topleft=(440, 269))


yellow_light = pygame.Surface([7, 7])
yellow_light.fill(yellow)
yellow_light_rect = light.get_rect(topleft=(440, 269))

# traffic light left
light_onL = 0


lightL = pygame.Surface([10, 10])
lightL.fill((0, 0, 0))
light_rect_L = lightL.get_rect(topleft=(560, 220))

red_lightL = pygame.Surface([7, 7])
red_lightL.fill(red)
red_light_rect_L = lightL.get_rect(topleft=(560, 220))


green_lightL = pygame.Surface([7, 7])
green_lightL.fill(green)
green_light_rect_L = lightL.get_rect(topleft=(560, 220))


yellow_lightL = pygame.Surface([7, 7])
yellow_lightL.fill(yellow)
yellow_light_rect_L = lightL.get_rect(topleft=(560, 220))


# traffic light top
light_onT = 0


lightT = pygame.Surface([10, 10])
lightT.fill((0, 0, 0))
light_rect_T = lightT.get_rect(topleft=(470, 200))

red_lightT = pygame.Surface([7, 7])
red_lightT.fill(red)
red_light_rect_T = lightT.get_rect(topleft=(470, 200))


green_lightT = pygame.Surface([7, 7])
green_lightT.fill(green)
green_light_rect_T = lightT.get_rect(topleft=(470, 200))


yellow_lightT = pygame.Surface([7, 7])
yellow_lightT.fill(yellow)
yellow_light_rect_T = lightT.get_rect(topleft=(470, 200))

# traffic light down
light_onD = 0


lightD = pygame.Surface([10, 10])
lightD.fill((0, 0, 0))
light_rect_D = lightD.get_rect(topleft=(521, 297))

red_lightD = pygame.Surface([7, 7])
red_lightD.fill(red)
red_light_rect_D = lightD.get_rect(topleft=(521, 297))


green_lightD = pygame.Surface([7, 7])
green_lightD.fill(green)
green_light_rect_D = lightD.get_rect(topleft=(521, 297))


yellow_lightD = pygame.Surface([7, 7])
yellow_lightD.fill(yellow)
yellow_light_rect_D = lightD.get_rect(topleft=(521, 297))

# timers
# traffic
traffic_timer = pygame.USEREVENT + 0
pygame.time.set_timer(traffic_timer, 1500)

car_timer = pygame.USEREVENT + 1
pygame.time.set_timer(car_timer, 2000)

# start of the loop
while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == car_timer:
                screen.blit(car, car_rect)
                cars.append(car.get_rect(topleft=(10, 275)))

        if event.type == traffic_timer:

            light_onD += 1
            light_onT += 1
            light_onL += 1
            light_on += 1

            # down light
            if light_onD == 3:
                light_onD = 0

            if light_onD == 0:
                light_onD = 0
                light_onT = 0
                light_onL = 1
                light_on = 1

            if light_onD == 1:
                if light_on == 2 and light_onL == 2:
                    light_onD = 0
                elif light_on == 0 and light_onL == 0:
                    light_onD = 0
                else:
                    light_onD = 1

            if light_onD == 2:
                if light_on == 1 or light_onL == 1:
                    light_onL = 0
                    light_on = 0
                    light_onT = 2
                elif light_on == 0 and light_rect_L == 0:
                    light_onD = 2
                else:
                    light_onD = 0

            # from top
            if light_onT == 3:
                light_onT = 0

            if light_onT == 0:
                light_onD = 0
                light_onT = 0
                light_onL = 1
                light_on = 1

            if light_onT == 1:
                if light_on == 2 and light_onL == 2:
                    light_onT = 0
                elif light_on == 0 and light_onL == 0:
                    light_onT = 0
                else:
                    light_onT = 1

            if light_onT == 2:
                if light_on == 1 or light_onL == 1:
                    light_on = 0
                    light_onL = 0
                    light_onT = 2
                elif light_on == 0 and light_onL == 0:
                    light_onT = 2
                else:
                    light_onT = 0
                    light_on = 2
                    light_onL = 2

            if light_onL == 3:  # RED
                light_onL = 0  # RED

            if light_onL == 0:
                light_onL = 0
                light_on = 0

            if light_onL == 2:
                if light_onD == 2 or light_onT == 2:
                    light_onL = 2
                    light_onD = 0
                    light_onT = 0
                elif light_onD == 0 and light_onT == 0:
                    light_onL = 2
                else:
                    light_onL = 0

            if light_onL == 1:
                if light_onD == 2 and light_onT == 2:
                    light_onL = 0
                elif light_onD == 0 and light_onT == 0:
                    light_onL = 1
                else:
                    light_onL = 1

            if light_on == 3:
                light_on = 0

            if light_on == 0:
                light_onL = 0
                light_on = 0

            if light_on == 2:
                if light_onT == 1 or light_onD == 1:
                    light_on = 2
                    light_onD = 0
                    light_onT = 0
                elif light_onT == 0 and light_onD == 0:
                    light_on = 2
                else:
                    light_on = 0

            if light_on == 1:
                if light_onD == 2 and light_onT == 2:
                    light_on = 0
                elif light_onD == 0 and light_onT == 0:
                    light_on = 1
                else:
                    light_on = 1

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                if (start_time > 0):
                    break
                else:
                    nrOfAttempts += 1
                    start_time = int(pygame.time.get_ticks() / 1000)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            game_active = False

    if game_active:

        # drawing map
        screen.fill((86, 125, 70))
        screen.blit(roadFromLeft, roadFromLeft_rect)
        screen.blit(roadFromTop, roadFromTop_rect)
        screen.blit(roadOutlineHorizontal, roadOutlineHorizontal_rect)
        screen.blit(roadOutlineHorizontal, ((0, 290)))
        screen.blit(roadOutlineHorizontal, ((550, 190)))
        screen.blit(roadOutlineHorizontal, ((550, 290)))
        screen.blit(roadOutlineVertical, roadOutlineVertical_rect)
        screen.blit(roadOutlineVertical, (550, 0))
        screen.blit(roadOutlineVertical, (440, 300))
        screen.blit(roadOutlineVertical, (550, 300))
        screen.blit(car5, car_rect5)
        screen.blit(car4, car_rect4)
        screen.blit(car3, car_rect3)
        screen.blit(car2, car_rect2)
        screen.blit(car1, car_rect1)
        screen.blit(car, car_rect)
        score = display_score()
        high_score = update_score(score, high_score)

        # traffic light
        if light_on == 0:  # RED LIGHT
            light = screen.blit(red_light, red_light_rect)
            if car_rect.x < 420 or car_rect.x > 490:
                car_rect.x += 5
            if car_rect1.x < 420 or car_rect1.x > 490:
                car_rect1.x += 5
        elif light_on == 1:  # YELLOW LIGHT
            light = screen.blit(yellow_light, yellow_light_rect)
            if car_rect.x > 380 and car_rect.x < 490:
                car_rect.x += 3
            else:
                car_rect.x += 5
            if car_rect1.x > 380 and car_rect1.x < 490:
                car_rect1.x += 3
            else:
                car_rect1.x += 5
        elif light_on == 2:  # GREEN LIGHT
            light = screen.blit(green_light, green_light_rect)
            car_rect.x += 5
            car_rect1.x += 5

        if car_rect.x and car_rect1.x > 1100:
            car_rect.left = 10
            car_rect1.left = 10

        # traffic light from left
        if light_onL == 0:  # RED LIGHT
            lightL = screen.blit(red_lightL, red_light_rect_L)
            if car_rect2.x > 560 or car_rect2.x < 450:
                car_rect2.x -= 5
            if car_rect3.x > 560 or car_rect3.x < 450:
                car_rect3.x -= 5
        elif light_onL == 1:  # YELLOW LIGHT
            lightL = screen.blit(yellow_lightL, yellow_light_rect_L)
            if car_rect2.x > 530 and car_rect2.x < 600:
                car_rect2.x -= 3
            else:
                car_rect2.x -= 5
            if car_rect3.x > 530 and car_rect3.x < 600:
                car_rect3.x -= 3
            else:
                car_rect3.x -= 5
        elif light_onL == 2:  # GREEN LIGHT
            lightL = screen.blit(green_lightL, green_light_rect_L)
            car_rect2.x -= 5
            car_rect3.x -= 5

        if car_rect2.x and car_rect3.x < -100:
            car_rect2.left = 980
            car_rect3.left = 980

        # traffic light from top
        if light_onT == 0:  # RED LIGHT
            lightT = screen.blit(red_lightT, red_light_rect_T)
            if car_rect4.y > 220 or car_rect4.y < 180:
                car_rect4.y += 5
        elif light_onT == 1:  # YELLOW LIGHT
            lightT = screen.blit(yellow_lightT, yellow_light_rect_T)
            if car_rect4.y > 250 and car_rect4.y < 300:
                car_rect4.y += 3
            else:
                car_rect4.y += 5
        elif light_onT == 2:  # GREEN LIGHT
            lightT = screen.blit(green_lightT, green_light_rect_T)
            car_rect4.y += 5

        if car_rect4.y > 600:
            car_rect4.bottom = 15

            # traffic light from down
        if light_onD == 0:  # RED LIGHT
            lightD = screen.blit(red_lightD, red_light_rect_D)
            if car_rect5.y > 300 or car_rect5.y < 250:  # 0 - 500
                car_rect5.y -= 5
        elif light_onD == 1:  # YELLOW LIGHT
            lightD = screen.blit(yellow_lightD, yellow_light_rect_D)
            if car_rect5.y > 250 and car_rect5.y < 300:
                car_rect5.y -= 3
            else:
                car_rect5.y -= 5
        elif light_onD == 2:  # GREEN LIGHT
            lightD = screen.blit(green_lightD, green_light_rect_D)
            car_rect5.y -= 5

        if car_rect5.y < -100:
            car_rect5.bottom = 490

        # drawing roads
        pygame.draw.line(roadFromLeft, 'gold', (0, 45), (440, 45), 4)
        pygame.draw.line(roadFromLeft, 'gold', (560, 45), (1000, 45), 4)
        pygame.draw.line(roadFromTop, 'gold', (50, 0), (50, 190), 4)
        pygame.draw.line(roadFromTop, 'gold', (50, 300), (50, 500), 4)
        # -- top left --
        pygame.draw.line(roadFromLeft, 'gold', (1, 22), (10, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (20, 22), (30, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (40, 22), (50, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (60, 22), (70, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (80, 22), (90, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (100, 22), (110, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (120, 22), (130, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (140, 22), (150, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (160, 22), (170, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (180, 22), (190, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (200, 22), (210, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (220, 22), (230, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (240, 22), (250, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (260, 22), (270, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (280, 22), (290, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (300, 22), (310, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (320, 22), (330, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (340, 22), (350, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (360, 22), (370, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (380, 22), (390, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (400, 22), (410, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (420, 22), (430, 22), 1)
        # -- bottom left --
        pygame.draw.line(roadFromLeft, 'gold', (1, 72), (10, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (20, 72), (30, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (40, 72), (50, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (60, 72), (70, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (80, 72), (90, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (100, 72), (110, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (120, 72), (130, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (140, 72), (150, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (160, 72), (170, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (180, 72), (190, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (200, 72), (210, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (220, 72), (230, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (240, 72), (250, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (260, 72), (270, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (280, 72), (290, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (300, 72), (310, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (320, 72), (330, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (340, 72), (350, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (360, 72), (430, 72), 3)

        # -- right top --
        pygame.draw.line(roadFromLeft, 'gold', (1000, 22), (990, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (980, 22), (970, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (960, 22), (950, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (940, 22), (930, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (920, 22), (910, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (900, 22), (890, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (880, 22), (870, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (860, 22), (850, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (840, 22), (830, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (820, 22), (810, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (800, 22), (790, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (780, 22), (770, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (760, 22), (750, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (740, 22), (730, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (720, 22), (710, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (700, 22), (690, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (680, 22), (670, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (660, 22), (650, 22), 1)
        pygame.draw.line(roadFromLeft, 'gold', (640, 22), (570, 22), 3)

        # -- right left --
        pygame.draw.line(roadFromLeft, 'gold', (1000, 72), (990, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (980, 72), (970, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (960, 72), (950, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (940, 72), (930, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (920, 72), (910, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (900, 72), (890, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (880, 72), (870, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (860, 72), (850, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (840, 72), (830, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (820, 72), (810, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (800, 72), (790, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (780, 72), (770, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (760, 72), (750, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (740, 72), (730, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (720, 72), (710, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (700, 72), (690, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (680, 72), (670, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (660, 72), (650, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (640, 72), (630, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (620, 72), (610, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (600, 72), (590, 72), 1)
        pygame.draw.line(roadFromLeft, 'gold', (580, 72), (570, 72), 1)

        # -- upper road--
        pygame.draw.line(roadFromTop, 'gold', (50, 0), (50, 190), 4)

        pygame.draw.line(roadFromTop, 'gold', (23, 0), (23, 10), 1)
        pygame.draw.line(roadFromTop, 'gold', (23, 20), (23, 30), 1)
        pygame.draw.line(roadFromTop, 'gold', (23, 40), (23, 50), 1)
        pygame.draw.line(roadFromTop, 'gold', (23, 60), (23, 70), 1)
        pygame.draw.line(roadFromTop, 'gold', (23, 80), (23, 90), 1)
        pygame.draw.line(roadFromTop, 'gold', (23, 100), (23, 110), 1)
        pygame.draw.line(roadFromTop, 'gold', (23, 120), (23, 190), 3)

        pygame.draw.line(roadFromTop, 'gold', (73, 0), (73, 10), 1)
        pygame.draw.line(roadFromTop, 'gold', (73, 20), (73, 30), 1)
        pygame.draw.line(roadFromTop, 'gold', (73, 40), (73, 50), 1)
        pygame.draw.line(roadFromTop, 'gold', (73, 60), (73, 70), 1)
        pygame.draw.line(roadFromTop, 'gold', (73, 80), (73, 90), 1)
        pygame.draw.line(roadFromTop, 'gold', (73, 100), (73, 110), 1)
        pygame.draw.line(roadFromTop, 'gold', (73, 120), (73, 130), 1)
        pygame.draw.line(roadFromTop, 'gold', (73, 140), (73, 150), 1)
        pygame.draw.line(roadFromTop, 'gold', (73, 160), (73, 170), 1)
        pygame.draw.line(roadFromTop, 'gold', (73, 180), (73, 190), 1)

        # lower road
        pygame.draw.line(roadFromTop, 'gold', (50, 300), (50, 500), 4)

        pygame.draw.line(roadFromTop, 'gold', (23, 300), (23, 310), 1)
        pygame.draw.line(roadFromTop, 'gold', (23, 320), (23, 330), 1)
        pygame.draw.line(roadFromTop, 'gold', (23, 340), (23, 350), 1)
        pygame.draw.line(roadFromTop, 'gold', (23, 360), (23, 370), 1)
        pygame.draw.line(roadFromTop, 'gold', (23, 380), (23, 390), 1)
        pygame.draw.line(roadFromTop, 'gold', (23, 400), (23, 410), 1)
        pygame.draw.line(roadFromTop, 'gold', (23, 420), (23, 430), 1)
        pygame.draw.line(roadFromTop, 'gold', (23, 440), (23, 450), 1)
        pygame.draw.line(roadFromTop, 'gold', (23, 460), (23, 470), 1)
        pygame.draw.line(roadFromTop, 'gold', (23, 480), (23, 490), 1)
        pygame.draw.line(roadFromTop, 'gold', (23, 497), (23, 500), 1)

        pygame.draw.line(roadFromTop, 'gold', (73, 310), (73, 380), 3)
        pygame.draw.line(roadFromTop, 'gold', (73, 390), (73, 400), 1)
        pygame.draw.line(roadFromTop, 'gold', (73, 410), (73, 420), 1)
        pygame.draw.line(roadFromTop, 'gold', (73, 430), (73, 440), 1)
        pygame.draw.line(roadFromTop, 'gold', (73, 450), (73, 460), 1)
        pygame.draw.line(roadFromTop, 'gold', (73, 470), (73, 480), 1)
        pygame.draw.line(roadFromTop, 'gold', (73, 490), (73, 500), 1)
    else:
        screen.fill((4, 159, 65))
        start_time = 0
        light_on = 0
        car_rect.x = 0
        car_rect1.x = 0
        car_rect2.x = 990
        car_rect3.x = 990
        car_rect4.y = 10
        car_rect5.y = 490
        score_message_again = game_font.render(
            f'Press SPACE to start again', False, (65, 65, 65))
        score_message_again_rect = score_message_again.get_rect(
            center=(480, 260))
        score_message = game_font.render(
            f'Your score: {score}', False, (65, 65, 65))
        score_message_rect = score_message.get_rect(center=(480, 180))
        high_score_surface = game_font.render(
            f'High score: {high_score}', False, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center=(480, 340))

        if score == 0:
            screen.blit(game_name, game_name_rect)
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message_again, score_message_again_rect)
            screen.blit(score_message, score_message_rect)
            screen.blit(high_score_surface, high_score_rect)

    pygame.display.update()
    clock.tick(60)
