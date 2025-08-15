import pygame
import random
import sys

# Screen size
WIDTH, HEIGHT = 400, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 250)
GREEN = (0, 200, 0)
RED = (255, 0, 0)

# Bird
BIRD_RADIUS = 20
BIRD_X = 100
GRAVITY = 0.5
FLAP_STRENGTH = -10

# Pipes
PIPE_WIDTH = 70
PIPE_GAP = 150
PIPE_SPEED = 3
PIPE_INTERVAL = 1500  # milliseconds

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 32)

# Events
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, PIPE_INTERVAL)

class Bird:
    def __init__(self):
        self.y = HEIGHT//2
        self.vel = 0

    def flap(self):
        self.vel = FLAP_STRENGTH

    def update(self):
        self.vel += GRAVITY
        self.y += self.vel

    def draw(self):
        pygame.draw.circle(screen, RED, (BIRD_X, int(self.y)), BIRD_RADIUS)

    def get_rect(self):
        return pygame.Rect(BIRD_X-BIRD_RADIUS, self.y-BIRD_RADIUS, BIRD_RADIUS*2, BIRD_RADIUS*2)

class Pipe:
    def __init__(self):
        self.x = WIDTH
        self.height = random.randint(100, HEIGHT-PIPE_GAP-100)
        self.passed = False

    def update(self):
        self.x -= PIPE_SPEED

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, 0, PIPE_WIDTH, self.height))
        pygame.draw.rect(screen, GREEN, (self.x, self.height+PIPE_GAP, PIPE_WIDTH, HEIGHT-(self.height+PIPE_GAP)))

    def get_top_rect(self):
        return pygame.Rect(self.x, 0, PIPE_WIDTH, self.height)

    def get_bottom_rect(self):
        return pygame.Rect(self.x, self.height+PIPE_GAP, PIPE_WIDTH, HEIGHT-(self.height+PIPE_GAP))

def main():
    bird = Bird()
    pipes = []
    score = 0
    running = True

    while running:
        clock.tick(FPS)
        screen.fill(BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flap()
            if event.type == SPAWNPIPE:
                pipes.append(Pipe())

        bird.update()
        bird.draw()

        remove_pipes = []
        for pipe in pipes:
            pipe.update()
            pipe.draw()
            # Check collision
            if bird.get_rect().colliderect(pipe.get_top_rect()) or bird.get_rect().colliderect(pipe.get_bottom_rect()):
                messagebox = pygame.font.SysFont("Arial", 48).render("Game Over", True, RED)
                screen.blit(messagebox, (WIDTH//2 - 120, HEIGHT//2 - 50))
                pygame.display.flip()
                pygame.time.delay(2000)
                main()
            # Score
            if not pipe.passed and pipe.x + PIPE_WIDTH < BIRD_X:
                pipe.passed = True
                score += 1
            if pipe.x + PIPE_WIDTH < 0:
                remove_pipes.append(pipe)

        for pipe in remove_pipes:
            pipes.remove(pipe)

        # Draw score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Check if bird hits ground or ceiling
        if bird.y + BIRD_RADIUS > HEIGHT or bird.y - BIRD_RADIUS < 0:
            main()

        pygame.display.flip()

if __name__ == "__main__":
    main()
