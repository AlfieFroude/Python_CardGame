import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack Game - Alfie Froude")

GREEN = (10, 108, 3)

FPS = 60


CARD = pygame.image.load(os.path.join('Assets', '2C.png'))

def draw_window():
    WIN.fill(GREEN)
    WIN.blit(CARD, (300, 100))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pyg-ame.QUIT:
                run = False

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()