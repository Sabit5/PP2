# Draw circle - a red ball of size 50 x 50 (radius = 25) on white background. 
# When user presses Up, Down, Left, Right arrow keys on keyboard, 
# the ball should move by 20 pixels in the direction of pressed key. 
# The ball should not leave the screen, 
# i.e. user input that leads the ball to leave of the screen should be ignored
import pygame

pygame.init()

size = width, height = (800, 600)

WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode(size)
pygame.display.set_caption(r'Red Ball')

clock = pygame.time.Clock()

x = 0
y = 0
dx = 0
dy = 0
velocity = 20

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_LEFT or event.key == pygame.K_a):
            dy = 0
            dx = -1 * velocity
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
            dy = 0
            dx = 1 * velocity
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_UP or event.key == pygame.K_w):
            dx = 0
            dy = -1 * velocity
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_DOWN or event.key == pygame.K_s):
            dx = 0
            dy = 1 * velocity
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_r):
            dx = 0
            dy = 0

    screen.fill((0, 0, 0))
    y += dy
    x += dx
    if x > width-50:
        x = width-50
    if x < 0:
        x = 0
    if y > height-50:
        y = height-50
    if y < 0:
        y = 0
    ellipse = pygame.draw.ellipse(screen, RED, (x, y, 50, 50))
    clock.tick(60)
    pygame.display.update()
pygame.quit()