import pygame
import time
import random

pygame.init()

width, height = 20, 20
block_size = 30

screen = pygame.display.set_mode((width * block_size, height * block_size))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

def initialize_game():
    global x, y, direction, movement_timer, trail, food, speed, points
    x, y = 0, 0
    direction = "RIGHT"
    movement_timer = 0
    trail = []
    food = generate_new_food()
    speed = 0.3
    points = 0

def generate_new_food():
    return random.randint(0, width - 1), random.randint(0, height - 1)

initialize_game()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and direction != 'DOWN':
        direction = 'UP'
    elif keys[pygame.K_s] and direction != 'UP':
        direction = 'DOWN'
    elif keys[pygame.K_a] and direction != 'RIGHT':
        direction = 'LEFT'
    elif keys[pygame.K_d] and direction != 'LEFT':
        direction = 'RIGHT'
#    elif keys[pygame.K_UP]:
#        speed += 0.1
#        time.sleep(0.1)
#    elif keys[pygame.K_DOWN] and speed > 0.1:
#        speed -= 0.1
#        time.sleep(0.1)

    if time.time() - movement_timer > 0.1 / speed:
        trail.insert(0, (x, y))
        if len(trail) > 5:
            trail.pop()

        if direction == 'UP':
            y = (y - 1) % height
        elif direction == 'DOWN':
            y = (y + 1) % height
        elif direction == 'LEFT':
            x = (x - 1) % width
        elif direction == 'RIGHT':
            x = (x + 1) % width

        movement_timer = time.time()

        if (x, y) == food:
            food = generate_new_food()
            trail.append(trail[-1])
            points += 1
            #speed += 0.1

        if (x, y) in trail:
            initialize_game()

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 0), (food[0] * block_size, food[1] * block_size, block_size, block_size))
    for bx, by in trail:
        pygame.draw.rect(screen, (255, 182, 193), (bx * block_size, by * block_size, block_size, block_size))
    pygame.draw.rect(screen, (0, 0, 0), (x * block_size, y * block_size, block_size, block_size))

    font = pygame.font.Font(None, 36)
    points_text = font.render(f"Score: {points}", True, (0, 0, 0))
    screen.blit(points_text, (width * block_size - 150, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
