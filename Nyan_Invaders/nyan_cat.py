import pygame

class Nyan():

    def __init__(self, screen):
        """ Инициализация Nyan Cat """

        self.screen = screen
        self.image = pygame.image.load('images/nyan_cat.png')
        self.rect = self.image.get_rect()             # Получаем объект пушки
        self.screen_rect = screen.get_rect()                # Получаем объект экрана
        self.rect.centerx = self.screen_rect.centerx  # Размещаем пушку по центру экрана
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.move_right = False
        self.move_left = False

    def output(self):
         """ Отрисовка Nyan Cat """

         self.screen.blit(self.image, self.rect)

    def update_cat(self):
        """ Обновление позиции Nyan Cat """
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += 0.5
        if self.move_left and self.rect.left > self.screen_rect.left:
            self.center -= 0.5

        self.rect.centerx = self.center

    def create_cat(self):
        """ Размещение Nyan Cat по центру экрана"""
        self.center = self.screen_rect.centerx