import pygame
# Create music player with keyboard controller. 
# You have to be able to press keyboard: play, stop, next and previous as some keys. 
# Player has to react to the given command appropriately.
pygame.init()
pygame.mixer.init()
size = width, hight = (400, 200) 
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))

# shorthand = pygame.transform.scale(pygame.image.load("rightarm.jpg"), (400, 300))
# shorthand = pygame.transform.rotate(shorthand, 36)

# longhand = pygame.transform.scale(pygame.image.load("leftarm.jpg"), (50, 600))
# longhand = pygame.transform.rotate(longhand, -96)

pygame.display.set_caption('Media - Player')
music_list = [
    "Miley Cyrus - Flowers.mp3", 
    "Tate McRae - exes.mp3", 
    "Dua Lipa - Training Season.mp3"
]

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

c = 0

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == SONG_END:
            print('The song ended.')
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            c += 1
            if c > len(music_list) - 1:
                c = 0
            pygame.mixer.music.stop()
            pygame.mixer.music.load(music_list[c])
            pygame.mixer.music.play(-1)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            c -= 1
            if c < 0:
                c = len(music_list) - 1
            pygame.mixer.music.stop()
            pygame.mixer.music.load(music_list[c])
            pygame.mixer.music.play(-1)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pygame.mixer.music.pause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            pygame.mixer.music.unpause()


pygame.quit()