import sys, pygame
pygame.init()

def main():
    #set up title screen, make green
    size = width, height = 700, 700
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Level Up!")
    green = [0,255,0]
    screen.fill(green)
    pygame.display.update()

    font = pygame.font.Font(None, 20)
    text = font.render("Level Up!", 1, (0,0,0))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    screen.blit(text, textpos)

    screen.blit(background, (0, 0))
    pygame.display.flip()
