import pygame


# Main canvas of game project
WIDTH, HEIGHT = 800, 600
GAME_WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(" Tower Blocks")

# declaring FPS rate (frames per second)
FPS = 60

game_state = "Menu"

# exporting media files
LOGOTYPE = pygame.image.load("Assets/favicon.png")
MENU_BAKCGROUND = pygame.image.load("Assets/game_background.png") # 800 x 600
MENU_TITLE = pygame.image.load("Assets/title.png") # 530 x 59
START_BUTTON = pygame.image.load("Assets/start_button.png") # 210 x 49
START_BUTTON_HOVERED = pygame.image.load("Assets/start_button_hovered.png") # 210 x 49
LEADERBOARD_BUTTON = pygame.image.load("Assets/leaderboard_button.png") # 370 x 48
LEADERBOARD_BUTTON_HOVERED = pygame.image.load("Assets/leaderboard_button_hovered.png") # 370 x 48
GAME_BACKGROUND = pygame.image.load("Assets/menu_background.png") # 800 x 600
HEART = pygame.image.load("Assets/heart.png")
BLOCK = pygame.image.load("Assets/block.png")
PERFECT_BLOCK = pygame.image.load("Assets/block-perfect.png")

pygame.display.set_icon(LOGOTYPE)

def game_window():
    if game_state == "Menu":
        GAME_WINDOW.blit(MENU_BAKCGROUND, (0, 0))
        GAME_WINDOW.blit(MENU_TITLE, (140, 90))
        GAME_WINDOW.blit(LEADERBOARD_BUTTON, (215, 300))
        GAME_WINDOW.blit(START_BUTTON, (295, 230))
    mouse = pygame.mouse.get_pos()

    # Transition animation for START button
    if mouse[0] in range(295, 505) and mouse[1] in range(230, 280):
        GAME_WINDOW.blit(START_BUTTON_HOVERED, (295, 230))
    else:
        GAME_WINDOW.blit(START_BUTTON, (295, 230))

    # Transition animation for LEADERBOARD button
    if mouse[0] in range(215, 585) and mouse[1] in range(300, 348):
        GAME_WINDOW.blit(LEADERBOARD_BUTTON_HOVERED, (215, 300))
    else:
        GAME_WINDOW.blit(LEADERBOARD_BUTTON, (215, 300))


def main():
    lives_left = 3
    condition = True
    game_state = "Menu"
    clock = pygame.time.Clock()
    processing = True
    while processing:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                processing = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                # In-Game Session
                if mouse[0] in range(295, 505) and mouse[1] in range(230, 280):
                    game_state = "Game Process"
                    condition = False
                    
        game_window()
        if game_state == "Game Process":
            GAME_WINDOW.blit(GAME_BACKGROUND, (0, 0))
            if lives_left == 3:
                GAME_WINDOW.blit(HEART, (10, 10))
                GAME_WINDOW.blit(HEART, (65, 10))
                GAME_WINDOW.blit(HEART, (120, 10))
            GAME_WINDOW.blit(BLOCK, (306, 465))
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()