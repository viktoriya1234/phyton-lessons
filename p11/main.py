import random

import pygame

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

white = (255, 255, 255)
black = (0, 0, 0)

pokemon = pygame.image.load('images/jigglypuff.png')
pokemon_size = pokemon.get_width()

cursor_image = pygame.image.load('images/pokemon_ball.png')
pygame.mouse.set_visible(False)

pokemon_x = random.randint(0, screen_width - pokemon_size)
pokemon_y = random.randint(0, screen_height - pokemon_size)

clock_fps = 60
clock = pygame.time.Clock()

font_fps = pygame.font.SysFont('Calibri', 27)
font_points = pygame.font.SysFont('Arial', 27)

GHANGE_POSITION = pygame.USEREVENT + 1
pygame.time.set_timer(GHANGE_POSITION, 1500)

def cursor_draw():
    position = pygame.mouse.get_pos()
    x = position[0] - (cursor_image.get_width() / 2)
    y = position[1] - (cursor_image.get_height() / 2)
    screen.blit(cursor_image, (x, y))


points = {'user': 0, 'pc': 0}

game_over = False
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            mx = pos[0]
            my = pos[1]

            if ((mx > pokemon_x) and (mx < pokemon_x + pokemon_size)
                    and (my > pokemon_y) and (my < pokemon_y + pokemon_size)):

                pokemon_x = random.randint(0, screen_width - pokemon_size)
                pokemon_y = random.randint(0, screen_height - pokemon_size)
                print(mx, my)

                points['user'] += 1

        elif event.type == GHANGE_POSITION:
            pokemon_x = random.randint(0, screen_width - pokemon_size)
            pokemon_y = random.randint(0, screen_height - pokemon_size)

            points['pc'] += 1



    screen.fill(black)
    screen.blit(pokemon, (pokemon_x, pokemon_y))

    fps_text = f'{clock.get_fps():.1f}FPS'
    font_fps_text = font_fps.render(fps_text, True, white)
    screen.blit(font_fps_text, (screen_width - 100, 10))

    font_points_text = font_points.render(f"{points['user']} : {points['pc']}", True, white)
    screen.blit(font_points_text, (10, 10))

    cursor_draw()

    pygame.display.flip()
    clock.tick(clock_fps)
pygame.quit()
