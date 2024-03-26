import pygame
from pygame import *
import datetime as dt
pygame.init()

# Use the image attached below(Mickey mouse's clock version)!
# Create a simple clock application (only with minutes and seconds) 
# which is synchronized with system clock. Use Mickey's right hand as minutes arrow and left - as seconds. 
#For moving Mickey's hands you can use: pygame.transform.rotate more explanation: https://stackoverflow.com/a/54714144
siz = 0.6
siz = 1/siz

#mainclock
mc0 = pygame.image.load("mainclock.png")
x = mc0.get_size()[0]//siz
y = mc0.get_size()[1]//siz
# print(x, y)
mainclock = pygame.transform.scale(mc0, (x, y))
mainclock_rect = mainclock.get_rect()

#minutehand
mh0 = pygame.image.load("rightarm.jpg")
minutehand = pygame.transform.scale(mh0, (mh0.get_size()[0]//siz, mh0.get_size()[1]//siz))

#secondhand
sh0 = pygame.image.load("leftarm.jpg")
secondhand = pygame.transform.scale(sh0, (sh0.get_size()[0]//siz, sh0.get_size()[1]//siz))

date = dt.datetime.now()
sec = int(date.strftime("%S"))
min = int(date.strftime("%M"))
sec_angle = -4 -sec*6
min_angle = -54 - min*6

# print(f"Minutes {min} = {min_angle}")
# print(f"Seconds {sec} = {sec_angle}")

screen = display.set_mode((x, y))
display.set_caption("Mickey the clock")
# mainclock_rect = mainclock.get_rect(topleft=(0, 0))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    secondhand = pygame.transform.rotate(secondhand, sec_angle)
    secondhand_rect = secondhand.get_rect(topleft=(x//2- secondhand.get_size()[0]//2, y//2-secondhand.get_size()[1]//2))

    minutehand = pygame.transform.rotate(minutehand, min_angle)
    minutehand_rect = minutehand.get_rect(topleft=(x//2- minutehand.get_size()[0]//2, y//2- minutehand.get_size()[1]//2))

    screen.fill((255, 255, 255))
    screen.blit(mainclock, (0, 0))
    screen.blit(secondhand, (secondhand_rect))
    screen.blit(minutehand, (minutehand_rect))
    pygame.display.flip()

    pygame.time.delay(1000)
    sec_angle = -6
    min_angle = 0
    sec+=1
    if sec == 60:
        sec = 0
        min_angle = -6
    else:
        min_angle = 0
