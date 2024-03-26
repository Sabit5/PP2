# Create music player with keyboard controller. 
# You have to be able to press keyboard: play, stop, next and previous as some keys. 
# Player has to react to the given command appropriately.
import pygame

pygame.init()
size = width, hight = (400, 200) 
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Media Player')

pygame.mixer.init()  # Initialize mixer for sound

# Define your music files
music_files = ["Miley Cyrus - Flowers.mp3", "Tate McRae - exes.mp3", "Dua Lipa - Training Season.mp3"]
current_song = 0

# Key assignments (customize if needed)
PLAY_KEY = pygame.K_RIGHT
STOP_KEY = pygame.K_DOWN
NEXT_KEY = pygame.K_UP
PREV_KEY = pygame.K_LEFT

# Function to load and play the current song
def play_music():
    pygame.mixer.music.load(music_files[current_song])
    pygame.mixer.music.play()

# Function to handle the next song
def next_song():
    global current_song
    current_song = (current_song + 1) % len(music_files)
    play_music()

# Function to handle the previous song
def prev_song():
    global current_song
    current_song = (current_song - 1) % len(music_files)
    play_music()

# Initial song load
play_music()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == PLAY_KEY:
                pygame.mixer.music.unpause()  # Resume if paused
            elif event.key == STOP_KEY:
                pygame.mixer.music.pause()
            elif event.key == NEXT_KEY:
                next_song()
            elif event.key == PREV_KEY:
                prev_song()

pygame.quit()
