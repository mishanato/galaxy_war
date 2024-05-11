import pygame

# Игрок
class Player:
    def __init__(self, screen_width, screen_height):
        self.__sprite = pygame.transform.scale(
            pygame.image.load("sprites/space_ship.png").convert_alpha(),
            (screen_width // 5, screen_height // 9)
        )
        #self.__sprite.get_alpha()
        black = (0, 0, 0)
        white = (255, 255, 255)
        self.__sprite.set_colorkey(black)
        self.__rect = self.__sprite.get_rect()

        self.__rect.x = screen_width // 2 - self.__rect.width // 2
        self.__rect.y = screen_height - 80   # screen_height // 2 - self.__rect.height // 2

        self.__horizontal_move_flag = 0
        self.__speed = 30

    def check_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.__horizontal_move_flag = -1
            elif event.key == pygame.K_d:
                self.__horizontal_move_flag = 1


    def check_logic(self, screen_width, screen_height):
        if self.__rect.y < 0:
            self.__rect.y = 0
        elif self.__rect.y > screen_height - self.__rect.height:
            self.__rect.y = screen_height - self.__rect.height
        if self.__rect.x < 0:
            self.__rect.x = 0
        elif self.__rect.x > screen_width - self.__rect.width:
            self.__rect.x = screen_width - self.__rect.width

    def move(self):
        self.__rect.x += self.__speed * self.__horizontal_move_flag

        self.__horizontal_move_flag = 0



    def draw(self, screen):
       # pygame.draw.rect(screen, (255, 255, 255), self.__rect)
        screen.blit(self.__sprite, self.__rect)