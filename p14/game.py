import pygame
import random

IMAGES_PATH: str = 'images/'
screen_width: int = 600
screen_height: int = 700
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))


class Diamond:
    x: int = 0
    y: int = 0
    speed: int = 0
    image = None
    width: int = 0

    def __init__(self, image):
        self.image = image
        self.image = self.image.get_width()
        self.x = random.randint(0, screen_width - self.width)
        self.speed = random.randint(1, 4)

    def show(self):
        screen.blit(self.image, (self.x, self.y))

    def fall(self):
        self.y += self.speed


class Diamonds:
    images: list = []
    diamonds_list: list = []

    def __init__(self):
        self.load_images()

    def load_images(self):
        for i in ('8.png', '9.png', '11.png'):
            self.images.append(pygame.image.load((IMAGES_PATH + i)))

    def add(self):
        img = self.images[random.randint(0, len(self.images)-1)]
        self.diamonds_list.append(Diamond(img))

    def draw(self):
        for item in self.diamonds_list:
            item.show()

    def fall(self):
        pass

    def delete(self):
        pass


class Wizard:
    x: int = 0
    y: int = 500
    speed: int = 10
    width: int = 0
    height: int = 0
    image_name: str = "1_IDLE_000.png"
    image = None

    def __init__(self):
        self.image_load()

    def image_load(self):
        self.image = pygame.image.load(IMAGES_PATH + self.image_name)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = int(screen_width / 2 - self.width / 2)

    def show(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self, direction: str):
        if direction == 'left':
            self.move_left()
        elif direction == 'right':
            self.move_right()

    def move_left(self):
        if self.x - self.speed >= 0:
            self.x -= self.speed
        else:
            self.x = 0

    def move_right(self):
        if self.x + self.speed <= screen_width - self.width:
            self.x += self.speed
        else:
            self.x = screen_width - self.width


class Game:
    run: bool = True
    background = None
    fps: int = 60
    clock = pygame.time.Clock()
    player: Wizard
    player_direction: str = ''

    def __init__(self):
        pygame.display.set_caption('Wizard')
        self.background_add(IMAGES_PATH + 'background.png')

    def background_add(self, image: str):
        self.background = pygame.image.load(image)

        self.player = Wizard()

    def background_draw(self, xy: tuple = (0, 0)):
        screen.blit(self.background, xy)

    def play(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player_direction = 'left'
                    if event.key == pygame.K_RIGHT:
                        self.player_direction = 'right'
                elif event.type == pygame.KEYUP:
                    self.player_direction = ''

            if self.run:
                self.background_draw()
                self.player.move(self.player_direction)
                self.player.show()

                pygame.display.update()
                self.clock.tick(self.fps)

        pygame.quit()


g = Game()
g.play()
