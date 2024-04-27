import pygame

IMG_LOCATION = 'Sprites/location/'
IMG_SHIP = 'Sprites/ship/s1/'
pygame.init()
screen = pygame.display.set_mode((600, 600))

img1 = pygame.image.load(IMG_LOCATION + 'bg-02.jpeg')
img2 = pygame.image.load(IMG_SHIP + 'Ship1.png')

img3 = pygame.image.load(IMG_SHIP + 'Ship2.png')
img3 = pygame.transform.rotate(img3, 60)
deg = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                deg += 1
            img3 = pygame.transform.rotate(img3, deg)

        screen.fill((127, 127, 127))
        screen.blit(img1, (20, 100))
        screen.blit(img2, (120, 200))
        screen.blit(img3, (120, 400))
        pygame.display.update()