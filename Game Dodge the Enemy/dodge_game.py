import pygame 
import random
import sys

# Initialize Pygame
pygame.init()

# Set screen size
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🚧 Dodge the Enemy")

# Colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()

# Player settings
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - player_size]

# Enemy settings
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 5

score = 0
font = pygame.font.SysFont("Arial", 30)

def detect_collision(player_pos, enemy_pos):
    px, py = player_pos
    ex, ey = enemy_pos

    return (px < ex + enemy_size and
            px + player_size > ex and
            py < ey + enemy_size and
            py + player_size > ey)

def show_score(score):
    label = font.render("Score: " + str(score), True, BLACK)
    screen.blit(label, (10, 10))

def game_over():
    label = font.render("Game Over!", True, RED)
    screen.blit(label, (WIDTH//2 - 80, HEIGHT//2))
    pygame.display.update()
    pygame.time.delay(2000)
    sys.exit()

# Game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= 7
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += 7

    # Enemy movement
    enemy_pos[1] += enemy_speed

    if enemy_pos[1] > HEIGHT:
        enemy_pos[1] = 0
        enemy_pos[0] = random.randint(0, WIDTH - enemy_size)
        score += 1
        enemy_speed += 0.3  # Increase difficulty

    # Collision detection
    if detect_collision(player_pos, enemy_pos):
        game_over()

    # Draw player and enemy
    pygame.draw.rect(screen, BLUE, (*player_pos, player_size, player_size))
    pygame.draw.rect(screen, RED, (*enemy_pos, enemy_size, enemy_size))

    show_score(score)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
