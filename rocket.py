import pygame


class rocket:
    def __init__(self, player_x, screen_width, screen_height, screen):
        self.__player_x = player_x
        self.__width = screen_width
        self.__height = screen_height

        self.__screen = screen

        self.__sprite = pygame.transform.scale(
            pygame.image.load("sprites/rocket.png").convert_alpha(),
            (screen_width // 10, screen_height // 10)
        )
        self.__rect = self.__sprite.get_rect()
        self.__rect.x = self.__player_x
        self.__rect.y = screen_height - 100

        self.__horizontal_move_flag = 0
        self.__speed = 1

        self.__draw_rk_flag = 1

    '''def check_event(self, event):
        if self.__draw_rk_flag == 1:
            self.draw()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.draw()
                self.__draw_rk_flag = 1
                print("ракета стартовала")
'''

    def move(self, player_x):
        self.__rect.x = player_x
        #self.__rect.y += self.__speed


    def draw(self):
        self.__screen.blit(self.__sprite, self.__rect)
        print("рисую пулю")