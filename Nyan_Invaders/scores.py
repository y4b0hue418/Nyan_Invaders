import pygame.font

class Scores():
    """ Вывод игровой информации """
    def __init__ (self, screen, stats):
        """ Инициализируем подсчёт очков """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (33, 39, 56)
        self.font = pygame.font.Font('font/PixeloidSans.ttf', 42)
        self.image_score()
        self.image_high_score()

    def image_score(self):
        """ Преобразовывает текст счёта в графическое изображение """
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (252, 164, 220))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def image_high_score(self):
        """"""
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (252, 164, 220))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = self.screen_rect.left - 20
        self.high_score_rect.top = 20

    def show_score(self):
        """ Отрисовка счёта на экране """
        self.screen.blit(self.score_img, self.score_rect)