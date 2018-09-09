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

    font = pygame.font.Font(None, 50)
    text = font.render("Level Up!", 1, (0,0,0))
    textpos = text.get_rect()
    textpos.centerx = screen.get_rect().centerx
    textpos.centery = screen.get_rect().centery
    screen.blit(text, textpos)

    pygame.display.flip()
