import pygame


def draw_background(screen, picture):
    screen.blit(picture, (0, 0))


class Wizard:
    x: int = 0
    y: int = 0
    speed: int = 0
    width: int = 0
    height: int = 0

    def move_left(self):
        pass

    def move_right(self):
        pass


def main():
    run = True

    pygame.init()
    screen_width: int = 600
    screen_height: int = 700
    screen = pygame.display.set_mode((screen_width, screen_height))
    background_picture = pygame.image.load('images/background.png')

    while run:
        draw_background(screen, background_picture)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


main()
