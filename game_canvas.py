import pygame


# Main canvas of game project
WIDTH, HEIGHT = 800, 600
GAME_WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Blocks")

# declaring FPS rate (frames per second)
FPS = 60
game_state = "Menu"
MENU_BAKCGROUND = pygame.image.load("Assets/menu_background.png")
MENU_TITLE = pygame.image.load("Assets/title.png")
START_BUTTON = pygame.image.load("Assets/start_button.png")
LEADERBOARD_BUTTON = pygame.image.load("Assets/leaderboard_button.png")


def game_window():
    GAME_WINDOW.blit(MENU_BAKCGROUND, (0, 0))
    GAME_WINDOW.blit(MENU_TITLE, (140, 90))
    GAME_WINDOW.blit(START_BUTTON, (295, 230))
    GAME_WINDOW.blit(LEADERBOARD_BUTTON, (215, 300))
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