import pygame


# Класс Игры
class Game:

    def __init__(self, width=800, height=600, bg_color=(200, 200, 200), fps=60):

        self.__width = width
        self.__height = height
        self.__bg_color = bg_color
        self.__screen = pygame.display.set_mode((self.__width, self.__height))
        self.__fps = fps
        self.__clock = pygame.time.Clock()

        self.__game_end = False

    def __del__(self):
        pygame.quit()

    def run(self):
        '''Метод для запуска игры'''
        while not self.__game_end:
            self.__check_events()
            self.__draw()

    # Проверка событий
    def __check_events(self):

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                self.__game_end = True

    # Отрисовка
    def __draw(self):

        self.__screen.fill(self.__bg_color)
        pygame.display.flip()


def main():
    '''Главная функция'''
    game = Game()
    game.run()


if "__main__" == __name__:
    main()