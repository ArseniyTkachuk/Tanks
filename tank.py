import pygame



# 0 - Пустий блок
# 1 - Блок який можна зруйнувати
# 2 - Блок який неможливо зруйнувати

map = [
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],#0
        [2,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,2],#1
        [2,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,2],#2
        [2,0,0,2,0,2,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,2,0,2,0,0,2],#3
        [2,0,0,2,0,2,1,1,1,1,1,2,2,1,1,2,2,1,1,1,1,1,2,0,2,0,0,2],#4
        [2,0,0,2,0,2,0,0,0,0,0,2,0,0,0,2,0,0,0,0,0,0,2,0,2,0,0,2],#5
        [2,0,0,2,0,2,0,0,0,0,0,2,0,0,0,2,0,0,0,0,0,0,2,0,2,0,0,2],#6
        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],#7
        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],#8
        [2,0,0,2,0,2,0,0,0,0,0,0,2,0,0,0,2,0,0,0,0,0,2,0,2,0,0,2],#9
        [2,0,0,2,0,2,0,0,0,0,0,0,2,0,0,0,2,0,0,0,0,0,2,0,2,0,0,2],#10
        [2,0,0,2,0,2,1,1,1,1,1,2,2,1,1,2,2,1,1,1,1,1,2,0,2,0,0,2],#11
        [2,0,0,2,0,2,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,2,0,2,0,0,2],#12
        [2,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,2],#13
        [2,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,2],#14
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],#15
#        0 1 2 3 4 5 6 7 8 9 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 
#                            0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 


        # [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]



        # [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]


        
        # [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        # [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
]




SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400
STEP = 25


window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tanks 2D')
pygame.display.set_icon(pygame.image.load('Tanks/images/tank.ico'))


class Block(pygame.Rect):
    def __init__(self, x, y, type_block, image):
        super().__init__(x, y, STEP, STEP)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (STEP, STEP))
        self.type_block = type_block
    def blit(self):
        window.blit(self.image, (self.x, self.y))
class Bullet(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, 10, 10)
        self.image = pygame.image.load( 'Tanks/images/bullet.png')
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.direction = None
        self.speed = 25
        self.count = 0
    def move(self):
        if self.count != 0:
            window.blit(self.image, (self.x, self.y))
            if self.direction == 0:
                self.y -= self.speed
            elif self.direction == 180:
                self.y += self.speed
            elif self.direction == 90:
                self.x -= self.speed
            elif self.direction == 270:
                self.x += self.speed
            self.count -= 1
            if self.count == 0:
                self.stop()
    def stop(self):
        self.count = 0
        self.x = 100000
class Panzar(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x * STEP, y * STEP, STEP, STEP)
        self.image = None
        self.pos = [x, y]
        self.bullet = Bullet(x, y)
        self.angle = 0
    def move(self):
        pass
    def blit(self):
        self.move()
        window.blit(self.image, (self.x, self.y))
    def rotate_to(self, angle):
        rotate = (360 - self.angle + angle)
        self.angle = angle
        self.image = pygame.transform.rotate(self.image, rotate)
    def strike(self):
        if self.bullet.count == 0:
            self.bullet.x = self.x + STEP / 2 - 5
            self.bullet.y = self.y + STEP / 2 - 5
            self.bullet.count = 15
            self.bullet.direction = self.angle
        
class Player(Panzar):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image =  pygame.image.load( 'Tanks/images/panzer.png')
        self.image =  pygame.transform.scale(self.image, (STEP, STEP))
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if map[self.pos[1] - 1][self.pos[0]] == 0:
                self.y -= STEP
                self.pos[1] -= 1
            self.rotate_to(0)
        elif keys[pygame.K_s]:
            if map[self.pos[1] + 1][self.pos[0]] == 0:
                self.y += STEP
                self.pos[1] += 1
            self.rotate_to(180)
        elif keys[pygame.K_a]:
            if map[self.pos[1]][self.pos[0] - 1] == 0:
                self.x -= STEP
                self.pos[0] -= 1
            self.rotate_to(90)
        elif keys[pygame.K_d]:
            if map[self.pos[1]][self.pos[0] + 1] == 0:
                self.x += STEP
                self.pos[0] += 1
            self.rotate_to(270)
        elif keys[pygame.K_x]:
            self.strike()
class Player2(Panzar):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image =  pygame.image.load('Tanks/images/enemy.png')
        self.image =  pygame.transform.scale(self.image, (STEP, STEP))
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if map[self.pos[1] - 1][self.pos[0]] == 0:
                self.y -= STEP
                self.pos[1] -= 1
            self.rotate_to(0)
        elif keys[pygame.K_DOWN]:
            if map[self.pos[1] + 1][self.pos[0]] == 0:
                self.y += STEP
                self.pos[1] += 1
            self.rotate_to(180)
        elif keys[pygame.K_LEFT]:
            if map[self.pos[1]][self.pos[0] - 1] == 0:
                self.x -= STEP
                self.pos[0] -= 1
            self.rotate_to(90)
        elif keys[pygame.K_RIGHT]:
            if map[self.pos[1]][self.pos[0] + 1] == 0:
                self.x += STEP
                self.pos[0] += 1
            self.rotate_to(270)
        elif keys[pygame.K_k]:
            self.strike()


pygame.init()

background = pygame.image.load('Tanks/images/background.png')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.Font(None, 120)
winner1_text = font.render('Синій виграв', True, (0,0,255))
winner2_text = font.render('Червоний виграв', True, (255,0,0))
Restart_text = font.render('Зіграти ще раз', True, (255,0,0))



x = 0
y = 0
blocks_list = []

wall_image1 = 'Tanks/images/wall.png'
wall_image2 = 'Tanks/images/wall1.png'

back = pygame.mixer.Sound('Tanks/sounds/back_music.wav')

for row in map:
    for i in row:
        if i == 1:
            blocks_list.append(Block(x, y, 1, wall_image1))
        elif i == 2:
            blocks_list.append(Block(x, y, 2, wall_image2))
        x += STEP
    y += STEP
    x = 0



player1  =  Player(1,1)
player2 = Player2(26,14)
clock = pygame.time.Clock()

is_game_running = True

game = 1

winner = None
while is_game_running:
    clock.tick(8)

    back.play()

    mous = pygame.mouse.get_pos()
    window.blit(background, (0,0))
    if game == 1 :
        for block in blocks_list:
            block.blit()
            if block.colliderect(player1.bullet):
                player1.bullet.stop()
                if block.type_block == 1:
                    map[block.y // STEP][block.x // STEP] = 0

                    block.x = 1000000
            if block.colliderect(player2.bullet):
                player2.bullet.stop()
                if block.type_block == 1:
                    map[block.y // STEP][block.x // STEP] = 0

                    block.x = 1000000
        player1.bullet.move()
        player2.bullet.move()
        player1.blit()
        player2.blit()
        if player1.colliderect(player2.bullet):
            winner = 2
            game = 2
        elif player2.colliderect(player1.bullet):
            winner = 1
            game = 2

    elif game == 2 :
        if winner == 1:
            window.blit(winner1_text, ( SCREEN_WIDTH // 2 - winner1_text.get_width() // 2, 
        SCREEN_HEIGHT // 4 - winner1_text.get_height()// 4))

            window.blit(Restart_text, ( SCREEN_WIDTH // 2 - Restart_text.get_width() // 2, 
        SCREEN_HEIGHT // 2 - Restart_text.get_height()// 2))
        
        elif winner == 2:
            window.blit(winner2_text, ( SCREEN_WIDTH // 2 - winner2_text.get_width() // 2, 
        SCREEN_HEIGHT // 2 - winner2_text.get_height()// 2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_running = False
    
    pygame.display.flip()
