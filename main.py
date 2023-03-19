import sys
import pygame
import background
import settings
import hero


class Game():
    """Основной класс игры"""

    def __init__(self):
        # Инициализируем фреймворк
        pygame.init()
        # Создаём экземпляр класса настроек игры
        self.gs = settings.Settings()
        # Создаём игровой экран
        self.screen = pygame.display.set_mode((self.gs.screen_width, self.gs.screen_height))
        # Создаём экземпляр класса фона игрового экрана
        self.bg = background.Background(self)
        # Задаём название для окна с игрой
        pygame.display.set_caption('The Chase')
        # Подгружаем изображение иконки
        self.icon = pygame.image.load('images/icon.jpg')
        # Устанавливаем иконку
        pygame.display.set_icon(self.icon)
        # Создание первого игрока
        self.player_1 = hero.Hero(self, 'images/kitty.png')

    def check_events(self):
        """Проверка действий игрока и реагирование на них"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_w:
                    self.player_1.direction_y = -1
                    self.player_1.move_y = True
                if event.key == pygame.K_s:
                    self.player_1.direction_y = 1
                    self.player_1.move_y = True
                if event.key == pygame.K_d:
                    self.player_1.direction_x = 1
                    self.player_1.move_x = True
                if event.key == pygame.K_a:
                    self.player_1.direction_x = -1
                    self.player_1.move_x = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.player_1.move_y = False
                if event.key == pygame.K_s:
                    self.player_1.move_y = False
                if event.key == pygame.K_d:
                    self.player_1.move_x = False
                if event.key == pygame.K_a:
                    self.player_1.move_x = False

    def run_game(self):
        """Запуск игры"""
        while True:
            # Прорисовать фон игрового экрана
            self.bg.show_back()
            # Прорисовать первого игрока
            self.player_1.show()
            # Прорисовать фон игрового экрана
            self.bg.show_front()
            # Обновить положение фона игрового экрана
            self.bg.update()
            # Обновить положение первого игрока
            self.player_1.move()
            # Обновление игрового экрана
            pygame.display.update()
            # Обработка действий игрока
            self.check_events()


game = Game()
game.run_game()






