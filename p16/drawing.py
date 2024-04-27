import pygame

pygame.init()
display = pygame.display.set_mode((600, 600), pygame.RESIZABLE)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.draw.rect(display, red, pygame.Rect(90, 30, 60, 50))
    pygame.draw.circle(display, blue, (150, 250), 70)
    pygame.draw.ellipse(display, green, (240, 190, 120, 90))
    for i in range(1, 11):
        pygame.draw.line(display, white, (60*i, 0), (60*i, 600), 2)
    pygame.display.update()