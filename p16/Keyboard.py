import pygame

pygame.init()
display = pygame.display.set_mode((100, 100), pygame.OPENGL)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
            print('down: ', key)
        if event.type == pygame.KEYUP:
            key = pygame.key.name(event.key)
            print('up: ', key)
