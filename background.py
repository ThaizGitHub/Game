import pygame
import settings


class Background():
    """Класс заднего фона игрового экрана"""

    def __init__(self, game):

        # Инициализация игрового экрана
        self.screen = game.screen
        # Инициируем игровые настройки
        self.gs = settings.Settings()

        # Инициализируем файлы слоёв фона
        self.bg_layer_1 = pygame.image.load('images/background/HillsLayer01.png').convert()
        self.bg_layer_2 = pygame.image.load('images/background/HillsLayer02.png').convert_alpha()
        self.bg_layer_2_copy = pygame.image.load('images/background/HillsLayer02.png').convert_alpha()
        self.bg_layer_3 = pygame.image.load('images/background/HillsLayer03.png').convert_alpha()
        self.bg_layer_3_copy = pygame.image.load('images/background/HillsLayer03.png').convert_alpha()
        self.bg_layer_4 = pygame.image.load('images/background/HillsLayer04.png').convert_alpha()
        self.bg_layer_4_copy = pygame.image.load('images/background/HillsLayer04.png').convert_alpha()
        self.bg_layer_5 = pygame.image.load('images/background/HillsLayer05.png').convert_alpha()
        self.bg_layer_5_copy = pygame.image.load('images/background/HillsLayer05.png').convert_alpha()
        self.bg_layer_6 = pygame.image.load('images/background/HillsLayer06.png').convert_alpha()
        self.bg_layer_6_copy = pygame.image.load('images/background/HillsLayer06.png').convert_alpha()

        # Координаты слоёв фона экрана
        self.bg_x = 0
        self.bg_2x = 0
        self.bg_4x = 0
        self.bg_6x = 0
        self.bg_8x = 0

    def show_back(self):
        """Отображает задние слои фона на игровом экране"""
        self.screen.blit(self.bg_layer_1, (0, 0))
        self.screen.blit(self.bg_layer_2, (self.bg_x, 0))
        self.screen.blit(self.bg_layer_2_copy, (self.bg_x + self.gs.screen_width, 0))
        self.screen.blit(self.bg_layer_3, (self.bg_2x, 0))
        self.screen.blit(self.bg_layer_3_copy, (self.bg_2x + self.gs.screen_width, 0))

    def show_front(self):
        """Отображает передние слои фона на игровом экране"""
        self.screen.blit(self.bg_layer_4, (self.bg_4x, 0))
        self.screen.blit(self.bg_layer_4_copy, (self.bg_4x + self.gs.screen_width, 0))
        # self.screen.blit(self.bg_layer_5, (self.bg_6x, 0))
        # self.screen.blit(self.bg_layer_5_copy, (self.bg_6x + self.gs.screen_width, 0))
        # self.screen.blit(self.bg_layer_6, (self.bg_8x, 0))
        # self.screen.blit(self.bg_layer_6_copy, (self.bg_8x + self.gs.screen_width, 0))

    def update(self):
        """Двигает фон"""
        self.bg_x -= 2
        self.bg_2x -= 4
        self.bg_4x -= 8
        self.bg_6x -= 12
        self.bg_8x -= 16

        if self.bg_x <= (-1 * self.gs.screen_width):
            self.bg_x = 0
        elif self.bg_2x <= (-1 * self.gs.screen_width):
            self.bg_2x = 0
        elif self.bg_4x <= (-1 * self.gs.screen_width):
            self.bg_4x = 0
        elif self.bg_6x <= (-1 * self.gs.screen_width):
            self.bg_6x = 0
        elif self.bg_8x <= (-1 * self.gs.screen_width):
            self.bg_8x = 0








