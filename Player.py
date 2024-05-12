import pygame
from rocket import *

# Игрок
class Player:
    def __init__(self, screen_width, screen_height, screen):
        self.__sprite = pygame.transform.scale(
            pygame.image.load("sprites/space_ship.png").convert_alpha(),
            (screen_width // 5, screen_height // 9)
        )
        #self.__sprite.get_alpha()
        black = (0, 0, 0)
        white = (255, 255, 255)
        self.__sprite.set_colorkey(black)
        self.__rect = self.__sprite.get_rect()

        self.__screen = screen

        self.__rect.x = screen_width // 2 - self.__rect.width // 2
        self.__rect.y = screen_height - 80   # screen_height // 2 - self.__rect.height // 2

        self.__speed = 30
        self.__horizontal_move_flag = 0
        self.__width = screen_width
        self.__height = screen_height

        self.__rocket = rocket(self.__rect.x, self.__width, self.__height, self.__screen)

    def check_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.__horizontal_move_flag = -1
            elif event.key == pygame.K_d:
                self.__horizontal_move_flag = 1
        self.__rocket.check_event(event)

    def check_logic(self, screen_width, screen_height):

        if self.__rect.x < 0:
            self.__rect.x = 0
        elif self.__rect.x > screen_width - self.__rect.width:
            self.__rect.x = screen_width - self.__rect.width

    def move(self):
        self.__rect.x += self.__speed * self.__horizontal_move_flag

        self.__horizontal_move_flag = 0



    def draw(self, screen):
       # pygame.draw.rect(screen, (255, 255, 255), self.__rect)
        # rk = pygame.Rect(200, 100, 30, 30)
        # screen.blit(screen, rk)
        screen.blit(self.__sprite, self.__rect)
       # self.__rocket.draw(screen)