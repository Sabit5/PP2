import pygame as pg
import random

pg.init()

def main():
    # Settings
    width, height = 400, 600
    FPS = 60
    MAX_SPEED = 20
    SPEED = 5
    ENEMY_SPEED = 2
    MAX_ENEMY_SPEED = 4
    SCORE = 0
    LEVEL = 0
    COINS_COLLECTED = 0
    running = True
    dead = False
    Oy = 0
    counter = SCORE

    # Music
    pg.mixer.music.load("music.mp3")
    pg.mixer.music.play(-1)
    pg.mixer.music.set_volume(0.03)

    # Sounds
    CarCrash_sound = pg.mixer.Sound("carcrash.mp3")
    CarCrash_sound.set_volume(0.05)

    # Fonts
    font_of_score = pg.font.SysFont('Arial', 22, bold=True)
    font_of_level = pg.font.SysFont('Arial', 22, bold=True)
    font_of_end = pg.font.SysFont('Arial', 50, bold=True)
    
    # Renders
    render_end = font_of_end.render('GAME OVER', True, pg.Color('red'))


    # Display
    clock = pg.time.Clock()
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("Racer")
    bg1 = pg.image.load("AnimatedStreet.png")
    bg2 = pg.image.load("AnimatedStreet.png")



    # Player class
    class Player(pg.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pg.image.load("Player.png")
            self.rect = self.image.get_rect()
            self.rect.center = (160, 520)

        def move(self):
            k = pg.key.get_pressed()
            if k[pg.K_LEFT] or k[pg.K_a]:
                if self.rect.left > 44:
                    self.rect.move_ip(-7, 0)
            if k[pg.K_RIGHT] or k[pg.K_d]:
                if self.rect.right < 356:
                    self.rect.move_ip(7, 0)
            if k[pg.K_UP] or k[pg.K_w]:
                if self.rect.top > 0:
                    self.rect.move_ip(0, -7)
            if k[pg.K_DOWN] or k[pg.K_s]:
                if self.rect.bottom < 600:
                    self.rect.move_ip(0, 7)

    # Enemy class
    class Enemy(pg.sprite.Sprite):
        global ENEMY_SPEED
        def __init__(self, y):
            super().__init__()
            self.y0 = y
            self.image = pg.image.load("Enemy.png")
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(40, 360), self.y0)

        def move(self):
            
            self.rect.move_ip(0, SPEED + ENEMY_SPEED)
            if self.rect.top > 600:
                self.rect.center = (random.randint(40, 360), self.y0)

    # Coins class
    class Coins(pg.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.weight = random.randint(1, 2)  # Assign random weight to the coin
            self.radius = 15 * self.weight
            self.image = pg.Surface((self.radius * 2, self.radius * 2), pg.SRCALPHA)
            pg.draw.circle(self.image, pg.Color('yellow'), (self.radius, self.radius), self.radius)
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(40, 360), -50)

        def change(self):
            self.weight = random.randint(1, 2)  # Assign random weight to the coin
            self.radius = 15 * self.weight
            self.image = pg.Surface((self.radius * 2, self.radius * 2), pg.SRCALPHA)
            pg.draw.circle(self.image, pg.Color('yellow'), (self.radius, self.radius), self.radius)
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(40, 360), -50)

        def move(self):
            self.rect.move_ip(0, SPEED)
            if self.rect.top > 600:
                self.change()


    # Game objects
    player = Player()
    enemy1 = Enemy(-90)
    enemy2 = Enemy(-180)
    coin = Coins()

    # Groups
    enemies = pg.sprite.Group()
    enemies.add(enemy1, enemy2)
    coins = pg.sprite.Group()
    coins.add(coin)
    all_sprites = pg.sprite.Group()
    all_sprites.add(enemy1, enemy2, player, coin)

    INC_SPEED = pg.USEREVENT + 1
    pg.time.set_timer(INC_SPEED, 5000)

    # Main game loop
    while running:
        clock.tick(FPS)
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
            elif event.type == INC_SPEED and SPEED < MAX_SPEED:
                SPEED += 1

        if not dead:
            Oy += SPEED
            if Oy >= 600:
                Oy = 0

            screen.blit(bg1, (0, Oy))
            screen.blit(bg2, (0, Oy - 600))

            for entity in all_sprites:
                entity.move()
                screen.blit(entity.image, entity.rect)

            # Score
            render_score = font_of_score.render(f'SCORE: {SCORE}', True, pg.Color('black'))
            screen.blit(render_score, (10, 10))

            # Collision with coin
            if pg.sprite.spritecollideany(player, coins):

                pg.mixer.Sound("coin.mp3").play().set_volume(0.1)
                print(type(coin.weight))
                SCORE += coin.weight  # Increment score based on coin weight
                COINS_COLLECTED += coin.weight  # Increment coins collected based on coin weight

                if COINS_COLLECTED >= 10 and MAX_ENEMY_SPEED < 4:  # Check if player earned N coins to increase enemy speed
                    ENEMY_SPEED += 1
                    LEVEL += 1
                    COINS_COLLECTED = 0  # Reset the coins collected count
                coin.change()

            # Collision with enemy
            if pg.sprite.spritecollideany(player, enemies):
                pg.mixer.music.pause()
                CarCrash_sound.play()
                dead = True

        else:
            pg.draw.rect(screen, pg.Color("black"), (38, 250, 321, 55))
            screen.blit(render_end, (44, 250))
            if pg.key.get_pressed()[pg.K_r]:
                return main()

if __name__ == "__main__":
    main()
