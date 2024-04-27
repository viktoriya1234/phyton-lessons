import pygame

pygame.init()
display = pygame.display.set_mode((100, 100), pygame.OPENGL)
pygame.display.set_caption('Mouse')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print('x={}, y={} '.format(pos[0], pos[1]))

