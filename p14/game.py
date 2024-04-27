import pygame
import random

IMAGES_PATH: str = 'images/'
GRAVITATION = 1
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
        self.width = self.image.get_width()
        self.x = int(random.randint(0, screen_width - self.width))
        self.speed = random.randint(3, 7)

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
        for item in self.diamonds_list:
            item.fall()

    def delete(self):
        pass

    def check_collision(self, player):
        collision = 0
        for item in self.diamonds_list:
            if ((item.x >= player.x and item.x <= player.x + player.width) and
                    (item.y >= player.y and item.y <= player.y + player.height)):
                collision = 1
                self.diamonds_list.remove(item)
            elif item.y > screen_height:
                collision = -1
                self.diamonds_list.remove(item)

        return collision


class Wizard:
    x: int = 0
    y: int = 500
    speed: int = 10
    width: int = 0
    height: int = 0
    image_name: str = "1_IDLE_000.png"
    image = None
    image_left = None
    image_right = None

    def __init__(self):
        self.image_load()

    def image_load(self):
        self.image_right = pygame.image.load(IMAGES_PATH + self.image_name)
        self.image = self.image_right
        self.image_left = pygame.transform.flip(self.image_right, 180, 0)

        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = int(screen_width / 2 - self.width / 2)

    def show(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self, direction: str) -> object:
        if direction == 'left':
            self.image = self.image_left
            self.move_left()
        elif direction == 'right':
            self.image = self.image_right
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


class NewWizard(Wizard):
    max_y: int = 500
    count_jump: int = 0
    max_jump: int = 2

    def __init__(self):
        super().__init__()

    def move(self, direction: str):
        if direction == 'left':
            self.image = self.image_left
            self.move_left()
        elif direction == 'right':
            self.image = self.image_right
            self.move_right()

        if self.y < self.max_y:
            self.y += 3

        if self.y >= self.max_y:
            self.count_jump = 0

    def jump(self):
        if self.count_jump < self.max_jump:
            self.y -= 100
        self.count_jump += GRAVITATION


class Game:
    run: bool = True
    background = None
    fps: int = 60
    clock = pygame.time.Clock()
    player: Wizard
    player_direction: str = ''
    diamonds = None
    diamond_event = pygame.USEREVENT + 1
    lost: int = 0
    catch: int = 0

    def __init__(self):
        pygame.display.set_caption('Wizard')
        self.background_add(IMAGES_PATH + 'background.png')
        self.player = NewWizard()

        self.diamonds = Diamonds()
        self.diamonds_add()

    def background_add(self, image: str):
        self.background = pygame.image.load(image)

    def background_draw(self, xy: tuple = (0, 0)):
        screen.blit(self.background, xy)

    def diamonds_add(self):
        pygame.time.set_timer(self.diamond_event, random.randint(500, 2000))
        self.diamonds.add()

    def game_status(self):
        check = self.diamonds.check_collision(self.player)

        if check == 1:
            self.catch += 1
        elif check == -1:
            self.lost += 1

        font = pygame.font.SysFont('Arial', 40)
        massege = "Score: " + str(self.catch) + ' - ' + str(self.lost) + ' '
        text = font.render(massege, True, (255, 255, 255), (122, 11, 122))
        screen.blit(text, (10, 10))

    def play(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.player_direction = 'left'
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.player_direction = 'right'
                    if event.key == pygame.K_UP:
                        self.player.jump()
                elif event.type == pygame.KEYUP:
                    self.player_direction = ''
                elif event.type == self.diamond_event:
                    self.diamonds_add()

            if self.run:
                self.background_draw()
                self.player.move(self.player_direction)
                self.player.show()
                self.diamonds.draw()
                self.diamonds.fall()
                self.game_status()

                pygame.display.update()
                self.clock.tick(self.fps)

        pygame.quit()


g = Game()
g.play()
