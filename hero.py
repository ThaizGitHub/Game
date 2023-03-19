import pygame
import settings


class Hero():
    """Класс игровых персонажей"""

    def __init__(self, game, skin):
        self.settings = settings.Settings()

        self.x = 500
        self.y = 400

        self.direction_x = 1
        self.direction_y = 1

        self.move_y = False
        self.move_x = False

        self.screen = game.screen
        self.skin = pygame.image.load(skin).convert_alpha()

    def show(self):
        """Отображает персонажа на экране"""
        self.screen.blit(self.skin, (self.x, self.y))

    def move(self):
        """Жвижение игрока"""
        self._check_edges()
        if self.move_x:
            self.x += 4 * self.direction_x
        if self.move_y:
            self.y += 4 * self.direction_y

    def _check_edges(self):
        """Ограничивает возможность игрока выйти за пределы экрана"""
        if self.x <= 0 and self.direction_x == -1:
            self.move_x = False
        elif self.x >= self.settings.screen_width - self.skin.get_width() and self.direction_x == 1:
            self.move_x = False
        if self.y <= 0 and self.direction_y == -1:
            self.move_y = False
        elif self.y >= self.settings.screen_height - self.skin.get_height() and self.direction_y == 1:
            self.move_y = False
