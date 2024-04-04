import pygame
pygame.init()

scrWidth = 600
scrHeight = 600
win = pygame.display.set_mode((scrWidth, scrHeight))

pygame.display.set_caption("My game")

rad = 30
vel = 20
x = 30
dx = 0
ey = 0
y = scrHeight-rad-150


isJump = False
jumpCount = 10

run = True
while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
            pygame.quit()
        
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > rad:
        dx = -vel
    if keys[pygame.K_RIGHT] and x < scrWidth-rad:
        dx = vel
    if not(isJump):
        # if keys[pygame.K_UP] and y > rad:
        #     y -= vel
        # if keys[pygame.K_DOWN] and y < scrHeight-rad:
        #     y += vel
        if keys[pygame.K_SPACE]: 
            isJump = True
        if keys[pygame.K_DOWN]:
            dx = 0
    else:
        neg = 1
        if jumpCount < 0:
            neg = -1
        if jumpCount >= -10:
            y -= (jumpCount**2)*0.5*neg
            jumpCount -= 1 
        else:
            isJump = False
            jumpCount = 10

    win.fill((0, 0, 0))
    x += dx
    if x >= scrWidth-rad:
        dx = 0
    if x <= rad:
        dx = 0 

    pygame.draw.circle(win, (255, 0, 0), (x, y), rad)
    pygame.display.update()
