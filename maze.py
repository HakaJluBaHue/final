#создай игру "Лабиринт"!
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
    "YOU WIN!" , True, (255,255,0)
)
lose = font.render(
    "YOU LOSE, TRY AGAIN!" , True, (255,0,0)
)
mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()
hero = Player("hero.png", 8, 1,1,70,70)
cyborg = Enemy("cyborg.png", 10, 630, 430,70,70)
treasure = Player("treasure.png", 0, 300, 220,100,100)
wall1 = wall(100,0,90,10,255,255,255)
wall2 = wall(100,90,10,90,255,255,255)
wall3 = wall(190,90,100,10,255,255,255)
wall4 = wall(190,190,10,100,255,255,255)
wall5 = wall(290,190,90,10,255,255,255)
wall5 = wall(290,280,10,250,255,255,255)
wall5 = wall(540,,,,255,255,255)
wall5 = wall(,,,,255,255,255)
wall5 = wall(,,,,255,255,255)
wall5 = wall(,,,,255,255,255)
wall5 = wall(,,,,255,255,255)
wall5 = wall(,,,,255,255,255)
wall5 = wall(,,,,255,255,255)
wall5 = wall(,,,,255,255,255)
wall5 = wall(,,,,255,255,255)
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
        if sprite.collide_rect(hero,cyborg) or sprite.collide_rect(hero,wall1) or sprite.collide_rect(hero,wall2) or sprite.collide_rect(hero,wall3) or sprite.collide_rect(hero,wall4) or sprite.collide_rect(hero,wall5):
            window.blit(lose,(50,200))
            finish = True



        hero.reset()
        cyborg.reset()
        cyborg.update()
        treasure.reset()
        hero.update()
        wall1.drawwall()
        wall2.drawwall()
        wall3.drawwall()
        wall4.drawwall()
        wall5.drawwall()
        display.update()
        clock.tick(FPS)
