import pygame


# Main canvas of game project
WIDTH, HEIGHT = 800, 600
GAME_WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Blocks")

# declaring FPS rate (frames per second)
FPS = 60


def game_window():
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    processing = True
    while processing:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                processing = False
                break
    
        game_window()
    pygame.quit()

if __name__ == "__main__":
    main()