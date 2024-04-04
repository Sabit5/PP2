import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Window size
window_x = 720
window_y = 480

# Defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Set up the game window
game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption('Snake Game')

# FPS (frames per second) controller
fps = pygame.time.Clock()

# Define the snake initial position, speed, and direction
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
snake_speed = 15
direction = 'RIGHT'
change_to = direction

# Initialize the fruit position, score, and level
fruit_position = [random.randrange(1, (window_x // 10) - 1) * 10, random.randrange(1, (window_y // 10) - 1) * 10]
score = 0
level = 1

# Displaying score and level function
def show_score_and_level(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score: ' + str(score) + '   Level: ' + str(level), True, color)
    score_rect = score_surface.get_rect()
    score_rect.topleft = (10, 10)
    game_window.blit(score_surface, score_rect)

# Game over function
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is: ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    # Update the direction of the snake
    direction = change_to

    # Move the snake
    if direction == 'UP':
        snake_position[1] -= 10
    elif direction == 'DOWN':
        snake_position[1] += 10
    elif direction == 'LEFT':
        snake_position[0] -= 10
    elif direction == 'RIGHT':
        snake_position[0] += 10

    # Check for collision with walls
    if snake_position[0] < 0 or snake_position[0] >= window_x or snake_position[1] < 0 or snake_position[1] >= window_y:
        game_over()

    # Check for collision with the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # Check for collision with the fruit
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        snake_body.insert(0, list(snake_position))
        fruit_position = [random.randrange(1, (window_x // 10) - 1) * 10, random.randrange(1, (window_y // 10) - 1) * 10]
        # Increase speed every 3-4 foods
        if score % 30 == 0:
            level += 1
            snake_speed += 5
    else:
        snake_body.insert(0, list(snake_position))
        snake_body.pop()

    # Display everything
    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, red, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))
    show_score_and_level(white, 'times new roman', 20)

    pygame.display.update()
    fps.tick(snake_speed)
