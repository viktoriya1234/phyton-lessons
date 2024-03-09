# --------------------------------------------------- #
#   * * *   *   *  * * *      *     **    **  * * *   #
#   *   *    * *   *   *     * *    * *  * *  *       #
#   * * *    **    *         * *    *  *   *  * * *   #
#   *        *     *  **    * * *   *  *   *  *       #
#   *       *      * * *   *     *  *      *  * * *   #
# --------------------------------------------------- #

import pygame
import sys

screen_width = 800
screen_height = 600
#  ініціалізація pygame
pygame.init()
# створюємо вікно
screen = pygame.display.set_mode((screen_width, screen_height))
# інтервал між кадрами
clock = pygame.time.Clock()
clock_tick = 60

pygame.display.set_caption('GTA_SPYDER v0.1')

spyder_img = pygame.image.load('images/spyder.png')
spyder_position = {'x': 10, 'y': 100}

# background = pygame.Surface((800, 600))
# background.fill('Black')
background = pygame.image.load('images/background.jpg')

count_fly = pygame.font.Font('fonts/MadimiOne-Regular.ttf', 50)
text_count_fly = count_fly.render('Count: 0', False, 'Black')

x = 10
y = 100

# ===============================================================================
while True:
    # перевіряємо події які відбулись в системі
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # 1. робимо розрахунки
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if spyder_position['y'] > 0:
            spyder_position['y'] -= 4
    if keys[pygame.K_s]:
        if spyder_position['y'] < screen_height - 110:
            spyder_position['y'] += 4
    if keys[pygame.K_a]:
        if spyder_position['x'] > 0:
            spyder_position['x'] -= 4
    if keys[pygame.K_d]:
        if spyder_position['x'] <screen_width - 110:
            spyder_position['x'] += 4

    # 2 добавляємо обєкти на екран
    screen.blit(background, (0, 0))
    screen.blit(spyder_img, (spyder_position['x'], spyder_position['y']))
    screen.blit(text_count_fly, (600, 10))

    # 3. оновлюємо область екрану
    pygame.display.update()
    clock.tick(clock_tick)