import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎯 Catch the Falling Objects")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 102, 204)
RED = (255, 0, 0)

# Game variables
bucket_width = 100
bucket_height = 20
bucket_x = WIDTH // 2 - bucket_width // 2
bucket_y = HEIGHT - bucket_height - 10
bucket_speed = 10

object_size = 20
object_x = random.randint(0, WIDTH - object_size)
object_y = -object_size
object_speed = 5

score = 0
missed = 0
max_misses = 5

font = pygame.font.SysFont("Arial", 24)
clock = pygame.time.Clock()

def draw_bucket(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, bucket_width, bucket_height))

def draw_object(x, y):
    pygame.draw.rect(screen, RED, (x, y, object_size, object_size))

def display_text(text, x, y, color=BLACK):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

def game_over():
    screen.fill(WHITE)
    display_text("Game Over! Final Score: " + str(score), WIDTH//2 - 150, HEIGHT//2)
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move bucket
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and bucket_x > 0:
        bucket_x -= bucket_speed
    if keys[pygame.K_RIGHT] and bucket_x < WIDTH - bucket_width:
        bucket_x += bucket_speed

    # Move object
    object_y += object_speed

    # Collision detection
    if (bucket_y < object_y + object_size and
        bucket_y + bucket_height > object_y and
        bucket_x < object_x + object_size and
        bucket_x + bucket_width > object_x):
        score += 1
        object_speed += 0.3  # Increase speed
        object_x = random.randint(0, WIDTH - object_size)
        object_y = -object_size

    # Missed object
    if object_y > HEIGHT:
        missed += 1
        object_x = random.randint(0, WIDTH - object_size)
        object_y = -object_size

    if missed >= max_misses:
        game_over()

    draw_bucket(bucket_x, bucket_y)
    draw_object(object_x, object_y)

    display_text("Score: " + str(score), 10, 10)
    display_text("Missed: " + str(missed), WIDTH - 120, 10)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
