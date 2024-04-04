import pygame
pygame.init()

#set of the screen
scrWidth = 500
scrHeight = 480
win = pygame.display.set_mode((scrWidth, scrHeight))
clock = pygame.time.Clock()
score = 0

#sounds
bulletSound = pygame.mixer.Sound('bullet.mp3')
bulletSound.set_volume(0.05)

hitSound = pygame.mixer.Sound("hit.mp3")
hitSound.set_volume(0.05) 
# bulletSound.play()
#music
music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.03)

#title of the app
pygame.display.set_caption("First Game")

#images of the character and background
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg') #background
char = pygame.image.load('standing.png') #characters


#Main character's class
class player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x+18, self.y+10, 28, 55)
    #drawing actions
    def draw(self, win):
        if self.walkCount+1 >= 27:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount+=1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (man.x, self.y))
                self.walkCount+=1
        else:
            # win.blit(char, (self.x, self.y))
            if self.left:
                win.blit(walkLeft[0], (self.x, self.y))
            else:
                win.blit(walkRight[0], (self.x, self.y))
        self.hitbox = (self.x+18, self.y+10, 28, 55)
    
    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = -16
        self.y = 400
        self.walkCount = 0
        font1 = pygame.font.SysFont('gigi', 100)
        text = font1.render('-5', 1, (255, 0, 0))
        win.blit(text, (250 - (text.get_width()//2), 200))
        pygame.display.update()
        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event .get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()

#Bullet's class
class projectile:
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing 
        self.vel = 15*facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    
#Enemy's class
class enemy:
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]
    
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.walkCount = 0
        self.vel = 3
        self.path = [100, self.end]    
        self.hitbox = (self.x+18, self.y+10, 28, 55)
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount +=1
            else: 
                win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            #healthbar
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1]-20, 50, 10))
            pygame.draw.rect(win, (0, 120, 0), (self.hitbox[0], self.hitbox[1]-20, 50 - (5*(10-self.health)), 10))
            self.hitbox = (self.x+14, self.y, 48, 60)
            # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
    def hit(self):
        if self.health > 1:
            self.health-=1
        else:
            self.visible = False
            #recreating the goblin
            global goblin
            goblin = enemy(450, 410, 64, 64, 450)



#Redrawing each frame
def redrawGameWin():
    #filling background
    win.blit(bg, (0, 0))
    #filling floor
    pygame.draw.rect(win, (100, 40, 0), (0, 460, 500, 480))
    #score text
    text = font.render('Score: ' + str(score), 1, (0, 0, 0))
    if score < 10:
        win.blit(text, (410, 10))
    elif score < 100:
        win.blit(text, (400, 10))
    else:
        win.blit(text, (390, 10))
    #drawing the man
    man.draw(win)
    #drawing a goblin
    goblin.draw(win)
    #drawing bullets
    for bullet in bullets:
        bullet.draw(win)
    

    pygame.display.update()



#list of bullets
bullets = []

#COOLDOWN MECHANISM
shootLoop = 0
coolDown = 3

#main loop
font = pygame.font.SysFont('gigi', 30, True, True)
man = player(-16, 400, 64, 64)
goblin = enemy(400, 404, 64, 64, 450)
run = True
while run:
    #setting fps 27 and calling redrawing function that makes a new frame
    clock.tick(27)
    redrawGameWin()

    if goblin.visible:
    #hiting the hitbox
        if man.hitbox[1] < goblin.hitbox[1]+goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
            if man.hitbox[0]+man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                man.hit()
                score -= 5


    #every frame and action is an event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    
    #bullets movement and removement, touching the goblin
    for bullet in bullets:
        #top and bottom of the bullet, hitting the hitbox  
        if goblin.visible: #this method also creates a new object
            #hiting the hitbox
            if bullet.y - bullet.radius < goblin.hitbox[1]+goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
                if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0]+goblin.hitbox[2]:
                    goblin.hit()
                    hitSound.play()
                    score+=1
                    bullets.pop(bullets.index(bullet))


        if bullet.x < 500 and bullet.x > 0:
            bullet.x+=bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    

        
    #Defining pressed button
    keys = pygame.key.get_pressed()

    #Getting buttons, therefore commands from user, SENDING SIGNALS

    #Bullet's keys
    if keys[pygame.K_SPACE] and shootLoop == 0:
        bulletSound.play()
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) <= 100:
            bullets.append(projectile(round(man.x + man.width//2), round(man.y + man.height//2), 5, (0, 0, 0), facing))
        shootLoop = coolDown

    if shootLoop > 0:
        shootLoop -= 1

    #Man's keys
    if keys[pygame.K_LEFT] and man.x > -16:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < scrWidth-54:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else: 
        man.standing = True
        man.walkCount = 0

    #JUMPING
    if not(man.isJump):
        if keys[pygame.K_UP]: 
            man.isJump = True
            man.left = False
            man.right = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
             #The jumping mechanism   
            man.y -= (man.jumpCount**2)*0.5*neg
            man.jumpCount -= 1 
        else:
            man.isJump = False
            man.jumpCount = 10
    

pygame.quit()
