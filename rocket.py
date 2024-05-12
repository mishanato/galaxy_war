import pygame


class rocket:
    def __init__(self, player_x, screen_width, screen_height, screen):
        self.__player_x_old = player_x
        self.__width = screen_width
        self.__height = screen_height

        self.__screen = screen

        self.__sprite = pygame.transform.scale(
            pygame.image.load("sprites/rocket.png").convert_alpha(),
            (screen_width // 15, screen_height // 20)
        )
        self.__rect = self.__sprite.get_rect()
        self.__rect.x = self.__player_x_old
        self.__rect.y = screen_height - 100

        self.__horizontal_move_flag = 0
        self.__speed = 5

        self.__draw_rk_flag = 1

    def check_event(self, event, player_pos, move_flag):
        self.__move_flag = move_flag
       # if self.__move_flag:
        #    self.__rect.x = player_pos



    def move(self, player_x):
      #  self.__rect.x = player_x
        self.__rect.y -= self.__speed


    def draw(self):
        if self.__move_flag:
            self.__screen.blit(self.__sprite, self.__rect)
       # print("рисую пулю")