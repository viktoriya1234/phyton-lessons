import sys
import pygame

PAINT_CIRCLE = 1001
CLEAR_CIRCLE = 123

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
pygame.init()
screen = pygame.display.set_mode((600, 400))
current_color = colors[0]

def draw_circle(action, color):
    if action == CLEAR_CIRCLE:
        color = (0, 0, 0)

    pos = pygame.mouse.get_pos()
    pygame.draw.circle(screen, color, pos, 18)
    pygame.display.update()


def change_color():
    global current_color

    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        current_color = colors[0]
    elif keys[pygame.K_2]:
        current_color = colors[1]
    elif keys[pygame.K_3]:
        current_color = colors[2]

def main():
    mouse_button = False


    while True:

        # --------------------------------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_button = True
                if event.button == 3:
                    pass
                    # draw_circle(CLEAR_CIRCLE, current_color)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_button = False
            elif event.type == pygame.KEYDOWN:
                change_color()


        # ------------------------------------------------

        if mouse_button:
            draw_circle(PAINT_CIRCLE,  current_color)


main()

