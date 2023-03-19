import pygame


class Hero():
    """Класс игровых персонажей"""

    def __init__(self, game, skin):
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
        if self.move_x:
            self.x += 4 * self.direction_x
        if self.move_y:
            self.y += 4 * self.direction_y