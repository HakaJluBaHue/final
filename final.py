from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, pl_image1, pl_speed, pl_x, pl_y, x, y):
        super().__init__()
        self.image = transform.scale(image.load(pl_image1),(x,y))
        self.speed = pl_speed
        self.rect = self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y <430:
            self.rect.y += self.speed
        if keys_pressed[K_LEFT] and self.rect.x >5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x <630:
            self.rect.x += self.speed


class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 1:
            self.side = "t1"
        elif self.rect.x >= 630 :
            self.side = "t2"


        if self.side == "t2":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

    def update1(self):
        if self.rect.y <= 1:
            self.side = "t3"
        elif self.rect.y >= 200 :
            self.side = "t4"


        if self.side == "t4":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
    
    def update2(self):
        if self.rect.y <= 1:
            self.side = "t5"
        elif self.rect.y >= 430 :
            self.side = "t6"


        if self.side == "t6":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed




class wall(sprite.Sprite):
    def __init__ (self, wallx, wally, wallh, wallw, c1, c2, c3):
        super().__init__()
        self.wallh = wallh
        self.wallw = wallw
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.image = Surface((self.wallh, self.wallw))
        self.image.fill((c1,c2,c3))
        self.rect = self.image.get_rect()
        self.rect.x = wallx
        self.rect.y = wally
    def drawwall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    



window = display.set_mode((700,500))
display.set_caption("Лабиринт")
background = transform.scale(image.load ("background.jpg"), (700,500))
game = True
clock = time.Clock()
FPS = 60
font.init()
font=font.Font(None,70)
win = font.render(
    "Ты победил!!!" , True, (255,255,0)
)
lose = font.render(
    "Ты проиграл, попробуй еще" , True, (255,0,0)
)
hahahaha = font.render(
    "Хехехе, не все так просто" , True, (255,0,0)
)
xD = font.render(
    "Слишком сложно" , True, (255,0,0)
)
mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()
hero = Player("hero.png", 5, 1,1,50,50)
cyborg = Enemy("cyborg.png", 12, 630, 430,70,70)
cyborg1 = Enemy("cyborg.png", 8, 500, 1,70,70)
cyborg2 = Enemy("cyborg.png", 12, 300, 1, 70,70)
treasure = Player("treasure.png", 0, 390, 150 ,80,80)
treasure1 = Player("treasure.png", 0, 150, 420 ,80,80)
treasure2 = Player("treasure.png", 0, 110, 1 ,80,80)
wall1 = wall(100,0,10,90,255,255,255)
wall2 = wall(100,90,90,10,255,255,255)
wall3 = wall(190,90,10,100,255,255,255)
wall4 = wall(190,190,100,10,255,255,255)
wall5 = wall(290,190,10,90,255,255,255)
wall6 = wall(290,280,80,10,255,255,255)
wall18 = wall(370,280,110,10,255,255,255)
wall19 = wall(480,280,60,10,255,255,255)
wall7 = wall(540,280,10,50,255,255,255)
wall8 = wall(540,330,40,10,255,255,255)
wall9 = wall(580,80,10,330,255,255,255)

wall10 = wall(0,200,100,10,255,255,255)
wall11 = wall(100,200,10,100,255,255,255)
wall12 = wall(100,300,50,10,255,255,255)
wall13 = wall(150,300,10,110,255,255,255)
wall14 = wall(230,400,210,10,255,255,255)
wall15 = wall(440,400,10,80,255,255,255)
wall16 = wall(440,480,250,10,255,255,255)
wall17 = wall(690,50,10,440,255,255,255)
finish=False
while game:
    window.blit(background,(0,0))


    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        if sprite.collide_rect(hero,treasure):
            window.blit(win,(200,200))
            finish = True
        if sprite.collide_rect(hero,cyborg) or sprite.collide_rect(hero,cyborg1) or sprite.collide_rect(hero,cyborg2) or sprite.collide_rect(hero,wall1) or sprite.collide_rect(hero,wall2) or sprite.collide_rect(hero,wall3) or sprite.collide_rect(hero,wall4) or sprite.collide_rect(hero,wall5) or sprite.collide_rect(hero,wall6) or sprite.collide_rect(hero,wall7) or sprite.collide_rect(hero,wall8) or sprite.collide_rect(hero,wall9) or sprite.collide_rect(hero,wall10) or sprite.collide_rect(hero,wall11) or sprite.collide_rect(hero,wall12) or sprite.collide_rect(hero,wall13) or sprite.collide_rect(hero,wall14) or sprite.collide_rect(hero,wall15) or sprite.collide_rect(hero,wall16) or sprite.collide_rect(hero,wall17) or sprite.collide_rect(hero,cyborg1):
            window.blit(lose,(10,200))
            finish = True
        if sprite.collide_rect(hero, treasure1):
            window.blit(hahahaha,(25,200))
            finish = True
        if sprite.collide_rect(hero, treasure2):
            window.blit(xD,(170,200))
            finish = True


        hero.reset()
        cyborg.reset()
        cyborg.update()
        cyborg1.reset()
        cyborg1.update1()
        cyborg2.reset()
        cyborg2.update2()
        treasure.reset()
        treasure1.reset()
        treasure2.reset()
        hero.update()
        wall1.drawwall()
        wall2.drawwall()
        wall3.drawwall()
        wall4.drawwall()
        wall5.drawwall()
        wall6.drawwall()
        wall7.drawwall()
        wall8.drawwall()
        wall9.drawwall()
        wall10.drawwall()
        wall11.drawwall()
        wall12.drawwall()
        wall13.drawwall()
        wall14.drawwall()
        wall15.drawwall()
        wall16.drawwall()
        wall17.drawwall()
        wall18.drawwall()
        wall19.drawwall()
        display.update()
        clock.tick(FPS)
