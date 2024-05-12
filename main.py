import pygame
from Player import *




# Класс Игры
class Game:

    def __init__(self, width=420, height=700, bg_color=(200, 200, 200), fps=60):

        pygame.init()


        self.__width = width
        self.__height = height
        self.__bg_color = bg_color
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        self.__bg_sprite = pygame.transform.smoothscale(
            pygame.image.load("sprites/space.jpg").convert(),
            (self.__width, self.__height)
        )
        self.__scene = 0
        self.__font1 = pygame.font.SysFont("Arial", 36)
        self.__test_text = self.__font1.render("TEST", True, (255, 255, 255))
        self.__fps = fps
        self.__clock = pygame.time.Clock()

        self.__game_end = False

        self.__player = Player(self.__width, self.__height, self.__screen)
    def __del__(self):
        pygame.quit()


    def run(self):
        '''Метод для запуска игры'''
        while not self.__game_end:
            self.__check_events()
            self.__check_logic()
            self.__move_objects()
            self.__draw()

    def __check_logic(self):
        self.__player.check_logic(self.__width, self.__height)

    def __move_objects(self):
        self.__player.move()

    # Проверка событий
    def __check_events(self):

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("SPACE")

                elif event.key == pygame.K_0:
                    self.__scene = 0


                elif event.key == pygame.K_1:
                    self.__scene = 1

                elif event.key == pygame.K_2:
                    self.__scene = 2


            if event.type == pygame.QUIT:
                self.__game_end = True
            self.__player.check_event(event)

    # Отрисовка
    def __draw(self):
        if self.__scene == 0:
            self.__screen.fill(self.__bg_color)

        elif self.__scene == 1:
            self.__screen.blit(self.__bg_sprite, (0, 0))

        elif self.__scene == 2:
            self.__screen.blit(self.__test_text, (210, 350))

        self.__player.draw(self.__screen)
        pygame.display.flip()

def main():
    '''Главная функция'''
    game = Game()

    game.run()


if "__main__" == __name__:
    main()