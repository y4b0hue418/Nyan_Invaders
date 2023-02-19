import pygame, sys
from bullet import Bullet
from cookie import Cookie
import time

clock = pygame.time.Clock()


def events(screen, cat, bullets):
    """ Обработка событий"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Нажатие клавиши

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_d:
                cat.move_right = True
            if event.key == pygame.K_a:
                cat.move_left = True
            if event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, cat)
                bullets.add(new_bullet)

        # Отпускание клавиши

        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_d:
                cat.move_right = False
            if event.key == pygame.K_a:
                cat.move_left = False

# Обновление экрана

def update(bg_color, screen, stats, sc, cat, cookies, bullets):

    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    cat.output()
    cookies.draw(screen)
    pygame.display.flip()  # Отрисовка кадра
    clock.tick(300)

def update_bullets(screen, stats, sc, cookies, bullets):

    bullets.update()
    for bullet in bullets.copy():
         if bullet.rect.bottom == 1:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, cookies, True, True)
    if collisions:
        for cookies in collisions.values():
            stats.score += 10 * len(cookies)
        sc.image_score()
    if len(cookies) == 0:
        bullets.empty()
        create_cookies(screen, cookies)

def cat_kill(stats, screen, cat, cookies, bullets):
    if stats.cat_left > 0:
        stats.cat_left -= 1
        cookies.empty()
        bullets.empty()
        create_cookies(screen, cookies)
        cat.create_cat()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()


def update_cookies(stats, screen, cat, cookies, bullets):
    cookies.update()
    if pygame.sprite.spritecollideany(cat, cookies):
        cat_kill(stats, screen, cat, cookies, bullets)
    cookies_check(stats, screen, cat, cookies, bullets)

def cookies_check(stats, screen, cat, cookies, bullets):
    """ Проверка коллизии печенек и экрана """
    screen_rect = screen.get_rect()
    for cookie in cookies.sprites():
        if cookie.rect.bottom >= (screen_rect.bottom):
            cat_kill(stats, screen, cat, cookies, bullets)
            break

def create_cookies(screen, cookies):

    cookie = Cookie(screen)
    cookie_width = cookie.rect.width
    number_cookie_x = int((510 - 2 * cookie_width) / cookie_width)
    cookie_height = cookie.rect.height
    number_cookie_y = int((600 - 100 - 2 * cookie_height) / cookie_height)

    for row_numb in range(number_cookie_y - 2):
        for cookie_numb in range(number_cookie_x):
            cookie = Cookie(screen)
            cookie.x = cookie_width + (cookie_width * cookie_numb)
            cookie.y = cookie_height + (cookie_height * row_numb)
            cookie.rect.x = cookie.x
            cookie.rect.y = cookie.rect.height + (cookie.rect.height * row_numb)
            cookies.add(cookie)