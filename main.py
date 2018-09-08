import sys, pygame
pygame.init()

def main():
    #set up screen, make green
    size = width, height = 700, 700
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Level Up!")
    green = [0,255,0]
    screen.fill(green)
    pygame.display.update()
