import sys, pygame
pygame.init()

def main():
    intro_screen()

def intro_screen():
    size = width, height = 700, 700
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Level Up!")
    green = [0,255,0]
    screen.fill(green)
    pygame.display.update()

    title_font = pygame.font.Font(None, 50)
    title = title_font.render("Level Up!", 1, (0,0,0))
    titlepos = title.get_rect()
    titlepos.centerx = screen.get_rect().centerx
    titlepos.centery = screen.get_rect().centery
    screen.blit(title, titlepos)
    pygame.display.update()

    #start and quit buttons
    btn_font = pygame.font.Font(None, 30)
    start_text = btn_font.render("Start", 1, (0,0,0)))
    quit_text = btn_font.render("Quit", 1, (0,0,0))
    start_btn = pygame.draw.rect(screen, green, [1, 1, 1, 1])
    quit_btn = pygame.draw.rect(screen, green, [1, 1, 1, 1])
