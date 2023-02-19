import pygame

class Cookie(pygame.sprite.Sprite):
    """ Класс одной печеньки """

    def __init__(self, screen):
        """ Инициализируем и задаём начальную позицию """
        super(Cookie, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/cookie.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """ Вывод печеньки на экран """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ Перемещение пришельцев """
        self.y += 0.09
        self.rect.y = self.y
