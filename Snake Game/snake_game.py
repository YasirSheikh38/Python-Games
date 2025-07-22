import pygame
import time
import random

# Initialize pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# Snake & Food
snake_block = 20
snake_speed = 15

clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 30)

def score_display(score):
    value = score_font.render(f"Score: {score}", True, BLACK)
    win.blit(value, [10, 10])

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, GREEN, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [WIDTH / 6, HEIGHT / 3])

def game_loop():
    game_over = False
    game_close = False

    x = WIDTH // 2
    y = HEIGHT // 2
    x_change = 0
    y_change = 0

    snake_list = []
    length = 1

    food_x = round(random.randrange(0, WIDTH - snake_block) / 20.0) * 20
    food_y = round(random.randrange(0, HEIGHT - snake_block) / 20.0) * 20

    while not game_over:

        while game_close:
            win.fill(WHITE)
            message("Game Over! Press Q to Quit or R to Restart", RED)
            score_display(length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        # Movement
        x += x_change
        y += y_change

        # Wall collision
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        win.fill(WHITE)
        pygame.draw.rect(win, RED, [food_x, food_y, snake_block, snake_block])

        snake_head = [x, y]
        snake_list.append(snake_head)

        if len(snake_list) > length:
            del snake_list[0]

        # Self collision
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        score_display(length - 1)

        pygame.display.update()

        # Eating food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - snake_block) / 20.0) * 20
            food_y = round(random.randrange(0, HEIGHT - snake_block) / 20.0) * 20
            length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
game_loop()
