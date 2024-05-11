import pygame
import random
import time
import sys

IMAGES_PATH = 'images/'
SCREEN_HEIGHT = 508
SCREEN_WIDTH = 828
FPS = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


class Bullet:
    bullet = None

    def __init__(self, x: int, y: int):
        self.bullet = pygame.Surface((8, 15))
        self.bullet.fill((0, 0, 50))
        self.x = x + 40
        self.y = y
        self.speed = 2

    def move(self):
        self.y -= self.speed

    def draw(self):
        screen.blit(self.bullet, (self.x, self.y))


class Bullets:
    bullet_list: list = []

    def add(self, x: int, y: int):
        self.bullet_list.append(Bullet(x, y))

    def move(self):
        for b in self.bullet_list:
            b.move()

            if b.y < 0:
                self.bullet_list.remove(b)
            b.draw()


class Player:
    delta_time = 1
    moving: int = ''
    bullets = None

    def __init__(self):
        n = random.randint(0, 4)
        image = pygame.image.load(IMAGES_PATH + f'Hull_0{n}.png')
        self.image = pygame.transform.scale(image, (100, 100))
        self.x = int(SCREEN_WIDTH / 2)
        self.y = SCREEN_HEIGHT - (self.image.get_height() + 10)
        self.speed = 5

        self.bullets = Bullets()

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        if self.moving == pygame.K_LEFT:
            self.move_left()
        if self.moving == pygame.K_RIGHT:
            self.move_right()

        self.bullets.move()

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

    def shoot(self):
        self.bullets.add(self.x, self.y)


class Background:
    background_image = None
    bg_surface = None

    def __init__(self):
        self.bg_image2 = None
        self.x = 0
        self.y = -SCREEN_HEIGHT * 2
        self.speed = 1
        self.bg_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT * 3))

        self.add_background()

    def add_background(self):
        self.background_image = pygame.image.load(IMAGES_PATH + 'bg-title-1.jpg')
        self.bg_surface.blit(self.background_image, (0, 0))
        #self.bg_surface.blit(self.background_image, (0, 1016))

    def background_draw(self, xy: tuple = (0, 0)):
        self.y += self.speed

        if self.y >= 0:
            self.y = -SCREEN_HEIGHT * 2

        screen.blit(self.bg_surface, (self.x, self.y))


class Game:
    game_run: bool = False
    bg_game = None

    def __init__(self):
        self.player = Player()
        self.bg_game = Background()
        self.dt = 1
        self.interval = time.time()

    def delta_time(self):
        clock.tick(FPS)
        self.dt = time.time() - self.interval
        self.interval = time.time()

        self.player.dt = self.dt

    def menu(self):
        im = pygame.image.load(IMAGES_PATH + 'bg_menu_1.jpg')
        screen.blit(im, (0, 0))
        font = pygame.font.SysFont('Arial', 20)
        text = font.render('- S', True, 'white')
        screen.blit(text, (290, 126))

    def init(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.run()

            self.menu()
            pygame.display.update()

    def run(self):
        self.game_run = True

        while self.game_run:
            self.delta_time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.moving = pygame.K_LEFT
                    if event.key == pygame.K_RIGHT:
                        self.player.moving = pygame.K_RIGHT
                    if event.key == pygame.K_SPACE:
                        self.player.shoot()
                    if event.key == pygame.K_q:
                        self.game_run = False
                        break
                elif event.type == pygame.KEYUP:
                    self.player.moving = 0

            if self.game_run:
                self.bg_game.background_draw()
                self.player.move()
                self.player.draw()

                pygame.display.update()

        # end while


if __name__ == '__main__':
    game = Game()
    game.init()
