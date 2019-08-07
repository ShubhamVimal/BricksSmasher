import pygame
import os


os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (400,50)

# Initialize Pygame
pygame.init()
SCREEN_WIDTH = 580
SCREEN_HEIGHT = 650
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RED = 255,0,0
WHITE = 255,255,255
BLACK = 0,0,0
BRICK_COLOUR = 0,255,0
GRAY = 220,217,217
BG_COLOUR = 64,64,64
BALL_COLOUR = 255,255,0

BG_IMG = pygame.image.load("bg.jpg")


def home_screen():
    game_name_font = pygame.font.SysFont('comicsansms',100)
    start_game_font = pygame.font.SysFont('comicsansms',55)
    game_name_text1 = 'Bricks'
    game_name_text2 = 'Smasher'
    start_game_text = 'Press Space to start'
    game_name_text1 = game_name_font.render(game_name_text1,True,WHITE)
    game_name_text2 = game_name_font.render(game_name_text2, True, WHITE)
    start_game_text = start_game_font.render(start_game_text,True,WHITE)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_run(1,0)

        screen.blit(BG_IMG, (0, 0))
        screen.blit(game_name_text1,(SCREEN_WIDTH//2-140,100))
        screen.blit(game_name_text2, (SCREEN_WIDTH//2-200, 200))
        screen.blit(start_game_text,(25,400))
        pygame.display.update()


def aestricBlock():
    font = pygame.font.SysFont(None,30)
    text_1 = font.render(
        '************************************************************************'
        ,True,WHITE)
    screen.blit(text_1,(2,10))
    text_2 = font.render('*',True,WHITE)
    screen.blit(text_2,(2,20))
    screen.blit(text_2,(570, 20))
    screen.blit(text_2,(2,30))
    screen.blit(text_2, (570, 30))
    screen.blit(text_2, (2, 40))
    screen.blit(text_2, (570, 40))
    screen.blit(text_2, (2, 50))
    screen.blit(text_2, (570, 50))
    screen.blit(text_1, (2, 60))


def level_name(level):
    font = pygame.font.Font('metropolis_regular.otf',25)
    text_1 = font.render('LEVEL {}'.format(level),True,RED)
    screen.blit(text_1,(SCREEN_WIDTH//2-40,30))


def player_score(c):
    font = pygame.font.Font('metropolis_regular.otf',25)
    text = font.render("Score : {}".format(c), True, RED)
    screen.blit(text, (15,30))


def playerLife(lives):
    msg = 'Lives: {}'.format(lives)
    font = pygame.font.Font('metropolis_regular.otf',25)
    text = font.render(msg,True,RED)
    screen.blit(text,(470,30))


def gameOver():
    game_over_msg_1 = 'GAME OVER'
    game_over_msg_2 = 'Press space to restart the Game'
    font_1 = pygame.font.SysFont('comicsansms',70)
    font_2 = pygame.font.SysFont('comicsansms',35)
    text_1 = font_1.render(game_over_msg_1,True,RED)
    text_2 = font_2.render(game_over_msg_2,True,RED)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_run(1,0)
        screen.blit(text_1, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2))
        screen.blit(text_2, (SCREEN_WIDTH // 2 - 265, SCREEN_HEIGHT // 2 + 100))
        pygame.display.update()


def display(level,lives,barX,barY,ballY,bricks):
    screen.fill(BG_COLOUR)
    aestricBlock()
    level_name(level)
    playerLife(lives)
    barRect = pygame.draw.rect(screen, WHITE, [barX, barY, 100, 10])
    pygame.draw.circle(screen, BALL_COLOUR, [ballX, ballY], 8)

    ballRect = pygame.Rect(ballX, ballY, 10, 10)

    for i in range(len(bricks)):
        pygame.draw.rect(screen, BRICK_COLOUR, bricks[i])

    return barRect,ballRect


def game_win():
    msg_1 = 'You WON'
    msg_2 = 'Press SPACE to restart the game'
    text_1 = pygame.font.Font('comicsansms',70).render(msg_1,True,RED)
    text_2 = pygame.font.Font('comicsansms',35).render(msg_2,True,RED)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_run(1,0)
        screen.blit(text_1, (SCREEN_WIDTH // 2 - 180, SCREEN_HEIGHT // 2))
        screen.blit(text_2, (SCREEN_WIDTH // 2 - 270, SCREEN_HEIGHT // 2 + 100))
        pygame.display.update()


def levels_generate(start_level):
    if start_level == 1:
        return level_1()
    elif start_level == 2:
        return level_2()
    elif start_level == 3:
        return level_3()
    elif start_level == 4:
        return level_4()
    elif start_level == 5:
        return level_5()
    elif start_level == 6:
        return game_win()


def level_1():
    BRICK_WIDTH = 60
    BRICK_HEIGHT = 20
    ROWS = 9
    COLS = SCREEN_WIDTH // BRICK_WIDTH
    BRICKS = []
    y_coord = 81
    for i in range(3, ROWS + 3):
        x_coord = 4
        for j in range(COLS):
            BRICKS.append(pygame.Rect(x_coord, y_coord, BRICK_WIDTH, BRICK_HEIGHT))
            x_coord += (BRICK_WIDTH + 4)
        y_coord += (BRICK_HEIGHT + 2)
    return BRICKS


def level_2():
    BRICK_WIDTH = 60
    BRICK_HEIGHT = 20
    ROWS = 7
    COLS = SCREEN_WIDTH // BRICK_WIDTH
    BRICKS = []
    y_coord_vertical = 104
    y_coord_horizontal = 81
    for i in range(3, ROWS + 3):
        x_coord_vertical = 55
        x_coord_horizontal = 4
        if i % 2 == 0:
            for j in range(COLS - 1):
                BRICKS.append(pygame.Rect(x_coord_vertical, y_coord_vertical, BRICK_HEIGHT, BRICK_WIDTH))
                x_coord_vertical += (BRICK_WIDTH + 4)
            y_coord_vertical += (BRICK_WIDTH + BRICK_HEIGHT + 6)
        else:
            for j in range(COLS):
                BRICKS.append(pygame.Rect(x_coord_horizontal, y_coord_horizontal, BRICK_WIDTH, BRICK_HEIGHT))
                x_coord_horizontal += (BRICK_WIDTH + 4)
            y_coord_horizontal += (BRICK_WIDTH + BRICK_HEIGHT + 6)
    return BRICKS


def level_3():
    BRICK_WIDTH = 60
    BRICK_HEIGHT = 20
    ROWS = 9
    COLS = SCREEN_WIDTH // BRICK_WIDTH
    BRICKS = []
    x_coord = 7
    y_coord = 81

    for i in range(ROWS):
        for j in range(COLS):
            BRICKS.append(pygame.Rect(x_coord, y_coord, BRICK_WIDTH, BRICK_HEIGHT))
            x_coord += (BRICK_WIDTH + 3)
        x_coord = (i + 1) * ((BRICK_WIDTH // 2) + 2)
        y_coord += (BRICK_HEIGHT + 2)
        COLS -= 1
    return BRICKS


def level_4():
    BRICK_WIDTH = 40
    BRICK_HEIGHT = 15
    BRICKS = []
    ROWS = 7
    COLS = 7

    y_coord = 81
    for i in range(ROWS - 1):
        x_coord = SCREEN_WIDTH // 2 - 42
        for j in range(COLS, i, -1):
            BRICKS.append(pygame.Rect(x_coord, y_coord, BRICK_WIDTH, BRICK_HEIGHT))
            x_coord -= (BRICK_WIDTH + 1)
        y_coord += (BRICK_HEIGHT + 2)
    y_coord = 81
    for i in range(ROWS - 1):
        x_coord = SCREEN_WIDTH // 2
        for j in range(COLS, i, -1):
            BRICKS.append(pygame.Rect(x_coord, y_coord, BRICK_WIDTH, BRICK_HEIGHT))
            x_coord += (BRICK_WIDTH + 1)
        y_coord += (BRICK_HEIGHT + 2)

    y_coord = 183
    for i in range(ROWS):
        x_coord = SCREEN_WIDTH // 2 - 42
        for j in range(0, i + 1):
            BRICKS.append(pygame.Rect(x_coord, y_coord, BRICK_WIDTH, BRICK_HEIGHT))
            x_coord -= BRICK_WIDTH + 1
        y_coord += BRICK_HEIGHT + 2
    y_ofs = 183
    for i in range(ROWS):
        x_ofs = SCREEN_WIDTH // 2
        for j in range(0, i + 1):
            BRICKS.append(pygame.Rect(x_ofs, y_ofs, BRICK_WIDTH, BRICK_HEIGHT))
            x_ofs += BRICK_WIDTH + 1
        y_ofs += BRICK_HEIGHT + 2
    return BRICKS


def level_5():
    BRICK_WIDTH = 40
    BRICK_HEIGHT = 20
    BRICKS = []
    ROWS = 7
    COLS = 7
    y_ofs = 81
    for i in range(ROWS):
        x_ofs = SCREEN_WIDTH // 2 - 42
        for j in range(0, i + 1):
            BRICKS.append(pygame.Rect(x_ofs, y_ofs, BRICK_WIDTH, BRICK_HEIGHT))
            x_ofs -= BRICK_WIDTH + 1
        y_ofs += BRICK_HEIGHT + 2

    y_ofs = 81
    for i in range(ROWS):
        x_ofs = SCREEN_WIDTH // 2
        for j in range(0, i + 1):
            BRICKS.append(pygame.Rect(x_ofs, y_ofs, BRICK_WIDTH, BRICK_HEIGHT))
            x_ofs += BRICK_WIDTH + 1
        y_ofs += BRICK_HEIGHT + 2

    y_coord = 235
    for i in range(ROWS):
        x_coord = SCREEN_WIDTH // 2 - 42
        for j in range(COLS, i, -1):
            BRICKS.append(pygame.Rect(x_coord, y_coord, BRICK_WIDTH, BRICK_HEIGHT))
            x_coord -= (BRICK_WIDTH + 1)
        y_coord += (BRICK_HEIGHT + 2)
    y_coord = 235
    for i in range(ROWS):
        x_coord = SCREEN_WIDTH // 2
        for j in range(COLS, i, -1):
            BRICKS.append(pygame.Rect(x_coord, y_coord, BRICK_WIDTH, BRICK_HEIGHT))
            x_coord += (BRICK_WIDTH + 1)
        y_coord += (BRICK_HEIGHT + 2)
    return BRICKS


def game_run(start_level,score):
    global ballX

    lives = 3
    FPS = 65
    clock = pygame.time.Clock()

    barX = (SCREEN_WIDTH//2) - 50
    barY = SCREEN_HEIGHT - 18
    barMoveX = 0

    ballY = barY - 10
    ballMoveX = 0
    ballMoveY = 0
    ballMove = False

    bricks = levels_generate(start_level)
    play = True
    while play:
        if not ballMove:
            ballX = barX + 50
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    barMoveX = 4
                elif event.key == pygame.K_LEFT:
                    barMoveX = -4
                elif event.key == pygame.K_SPACE:
                    ballMoveY = -4
                    ballMoveX = 4
                    ballMove = True
            elif event.type == pygame.KEYUP:
                barMoveX = 0

        barRect, ballRect = display(start_level,lives,barX,barY,ballY,bricks)

        barX += barMoveX
        ballX += ballMoveX
        ballY += ballMoveY

        for i in range(len(bricks)):
            if bricks[i].colliderect(ballRect):
                ballMoveY = 4
                score += 5
                FPS += 2
                del bricks[i]
                break

        player_score(score)

        if ballY < 10:
            ballMoveY = 4
        elif ballX < 10:
            ballMoveX = 4
        elif ballX > SCREEN_WIDTH - 10:
            ballMoveX = -4
        elif ballRect.colliderect(barRect):
            ballMoveY = -4
        elif barX < 0:
            barMoveX = 1
        elif barX > SCREEN_WIDTH - 100:
            barMoveX = -1
        elif ballY > SCREEN_HEIGHT:
            ballMove = False
            ballY = barY - 10
            ballMoveY = 0
            ballMoveX = 0
            lives -= 1

        playerLife(lives)
        if lives == 0:
            gameOver()
            play = False

        if len(bricks) == 0:
            start_level += 1
            break

        pygame.display.update()
        clock.tick(FPS)
    game_run(start_level,score)


home_screen()