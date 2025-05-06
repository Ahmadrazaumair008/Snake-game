import pygame
import random
import os

# initializing pygame

pygame.mixer.init()

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Background Image
bgimg = pygame.image.load("bg.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

# Intro Image

i_img = pygame.image.load("INTRO.png")
i_img = pygame.transform.scale(i_img, (screen_width, screen_height)).convert_alpha()

# gameover image 

goimg = pygame.image.load("GAMEOVER.png")
goimg = pygame.transform.scale(goimg, (screen_width, screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("Snake Game")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    pygame.mixer.music.load('bgm.mp3')
    pygame.mixer.music.play(-1)
    
    while not exit_game:
        gameWindow.blit(i_img, (0,0))  # This line draw intro image onto the window 

        # gameWindow.fill((233,210,229)
        # text_screen("Welcome to Snakes", black, 260, 250)
        # text_screen("Press ENTER To Play", black, 232, 290)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop() # Stop welcome music on quit
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.stop() # Stop welcome music                    
                    pygame.mixer.music.load('bgm1.mp3')
                    pygame.mixer.music.play(-1)
                    gameloop()

        pygame.display.update()
        clock.tick(60)

# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False

    snake_x = 45
    snake_y = 55
    
    velocity_x = 0
    velocity_y = 0
    
    snake_list = []
    snake_length = 1
    # Check if hiscore file exists
    if (not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")
    
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    food_x = random.randint(20, int(screen_width / 2))
    food_y = random.randint(20, int(screen_height / 2))
    score = 0
    init_velocity = 5
    snake_size = 20
    fps = 60
    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))

            # gameWindow.fill(white)

            gameWindow.blit(goimg, (0,0))  # This line draw the gameover image onto the window 
            
            # text_screen("Game Over! Press SPACE To Continue", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score +=10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score +=10
                food_x = random.randint(20, int(screen_width / 2))
                food_y = random.randint(20, int(screen_height / 2))
                snake_length +=5
                if score>int(hiscore):
                    hiscore = score
            
            # Game Window
            # gameWindow.fill(white)
            # bgimg = pygame.image.load("bg.jpg")
            # bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)). convert_alpha()
            gameWindow.blit(bgimg, (0, 0))

            text_screen("Score: " + str(score) + "  Hiscore: "+str(hiscore), white, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:    
                pygame.mixer.music.load('end.mp3')
                pygame.mixer.music.play()
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                pygame.mixer.music.load('end.mp3')
                pygame.mixer.music.play()
                game_over = True
            plot_snake(gameWindow, black, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
