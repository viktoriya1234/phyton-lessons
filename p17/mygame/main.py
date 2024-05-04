import pygame
import random
import time

IMAGES_PATH = 'images/'
SCREEN_HEIGHT = 508
SCREEN_WIDTH = 828
FPS = 500

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


class Player:
    delta_time = 1
    moving: int = ''

    def __init__(self):
        n = random.randint(0, 4)
        image = pygame.image.load(IMAGES_PATH + f'Hull_0{n}.png')
        self.image = pygame.transform.scale(image, (100, 100))
        self.x = int(SCREEN_WIDTH / 2)
        self.y = SCREEN_HEIGHT - (self.image.get_height() + 10)
        self.speed = 5

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        if self.moving == pygame.K_LEFT:
            self.move_left()
        if self.moving == pygame.K_RIGHT:
            self.move_right()

    def move_left(self):
        if self.x > 0:
            self.x -= self.speed
        else:
            self.x = 0

    def move_right(self):
        if self.x < SCREEN_WIDTH - self.image.get_width():
            self.x += self.speed
        else:
            self.x = SCREEN_WIDTH - self.image.get_width()

    def move_top(self):
        pass

    def move_down(self):
        pass

    def fire(self):
        pass


class Game:
    background_image = None

    def __init__(self):
        self.add_background()
        self.player = Player()
        self.dt = 1
        self.interval = time.time()

    def add_background(self):
        self.background_image = pygame.image.load(IMAGES_PATH + 'bg-title.png')

    def background_draw(self, xy: tuple = (0, 0)):
        screen.blit(self.background_image, xy)

    def delta_time(self):
        clock.tick(FPS)
        self.dt = time.time() - self.interval
        self.interval = time.time()

        self.player.dt = self.dt

    def init(self):
        while True:
            self.delta_time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.moving = pygame.K_LEFT
                    if event.key == pygame.K_RIGHT:
                        self.player.moving = pygame.K_RIGHT
                elif event.type == pygame.KEYUP:
                    self.player.moving = 0

            self.background_draw()
            self.player.move()
            self.player.draw()

            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.init()
