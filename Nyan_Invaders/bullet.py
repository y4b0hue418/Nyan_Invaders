import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, cat):
        """ Создаём пулю в позиции пушки"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 4, 20)
        self.color = 228, 0, 224
        self.speed = 0.9
        self.rect.centerx = cat.rect.centerx
        self.rect.centery = cat.rect.centery
        self.y = float(self.rect.y)

    def update(self):
        """ Перемещение пули вверх """
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """ Отрисовка пули """
        pygame.draw.rect(self.screen, self.color, self.rect)