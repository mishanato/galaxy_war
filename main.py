import pygame


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

    def move(self):
        self.__rect.x += self.__speed * self.__horizontal_move_flag

        self.__horizontal_move_flag = 0



    def draw(self, screen):
       # pygame.draw.rect(screen, (255, 255, 255), self.__rect)
        screen.blit(self.__sprite, self.__rect)


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

        self.__player = Player(self.__width, self.__height)
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