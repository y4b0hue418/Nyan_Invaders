import pygame, control
from nyan_cat import Nyan
from pygame.sprite import Group
from stats import Stats
from scores import Scores



# Функция инициализации

def run():

    pygame.init() # Инициализация
    screen = pygame.display.set_mode((510, 600)) # Установка параметров экрана
    pygame.display.set_caption('Nyan Invaders') # Заголовок окна
    bg_color = (252, 164, 220) # Цвет заднего фона
    cat = Nyan(screen) # ! Отрисовка на экране !
    bullets = Group()
    cookies = Group()
    control.create_cookies(screen, cookies)
    stats = Stats()
    sc = Scores(screen, stats)


    # Основной цикл игры

    while True:

        control.events(screen, cat, bullets) # Передвигаем пушку
        if stats.run_game:
            cat.update_cat()
            control.update(bg_color, screen, stats, sc, cat, cookies, bullets)
            control.update_bullets(screen, stats, sc, cookies, bullets)
            control.update_cookies(stats, screen, cat, cookies, bullets)



run()