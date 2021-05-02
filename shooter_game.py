from pygame import *
from random import randint
import time as pytime
from random import uniform
mixer.init()
lost = 0
class GameSprite(sprite.Sprite):
    def __init__(self,img,x,y,speed):
        super().__init__()
        self.image = transform.scale(image.load(img),(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def draw(self,window):
        window.blit(self.image,(self.rect.x,self.rect.y))
class HeroSprite(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT]:
            if self.rect.x >= 0:
                self.rect.x = self.rect.x - self.speed
        if keys_pressed[K_RIGHT]:
            if self.rect.x <= 750:
                self.rect.x = self.rect.x + self.speed
    def spawn_bullet(self):
        bullet = BulletSprite('bullet.png',self.rect.centerx,self.rect.top,3)
        bullets.add(bullet)
class EnemySprite(GameSprite):
    def update(self):
        self.rect.y = self.rect.y + self.speed
        global lost
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(50,750)
            self.speed = uniform(1,2)
            lost = lost + 1
        def kill(self):
            self.kill()
class BulletSprite(GameSprite):
    def update(self):
        self.rect.y = self.rect.y - self.speed
        if self.rect.y < 0:
            self.kill()
class AstroSprite(GameSprite):
    def update(self):
        self.rect.y = self.rect.y + self.speed
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(50,750)
            self.speed = randint(1,2)
window = display.set_mode((800,550))

background = transform.scale(image.load("galaxy.jpg"),(800,550))

run = True
clock = time.Clock()
FPS = 60

font.init()
font5 = font.SysFont('Arial',36)
font.init()
font2 = font.SysFont('Arial',36)
font.init()
font1 = font.SysFont('Arial',36)
font.init()
font3 = font.SysFont('Arial',100)
font.init()
font4 = font.SysFont('Arial',100)

old_time = pytime.time()

lifes = 3

mixer.music.load('space.ogg')
mixer.music.play()
shot = mixer.Sound('fire.ogg')

astrorocks = sprite.Group()
for a in range (0,2):
    astrorock = AstroSprite('asteroid.png',randint(0,750),0,randint(1,2))
    astrorocks.add(astrorock)
enemies = sprite.Group()
for e in range (0,5):
    enemy = EnemySprite('ufo.png',randint(0,750),0,uniform(1,2.3))
    enemies.add(enemy)

bullets = sprite.Group()
destroy_score = 0

finish = False
rocket = HeroSprite('cyborg.png',350,480,5)

while run:
    for e in event.get(): 
        if e.type == QUIT:
            run = False
    if finish != True:
        text_win = font3.render('ВЫ ВЫИГРАЛИ!!!',1,(255,255,255))
        text_proigral = font4.render('ВЫ ПРОИГРАЛИ :(',1,(255,255,255))
        window.blit(background,(0,0))
        text_lost = font1.render('Пропущено: '+ str(lost),1,(255,255,255))
        window.blit(text_lost,(15,50))
        keys_pressed = key.get_pressed()
        text_lifes = font5.render(str(lifes),1,(255,255,255))
        window.blit(text_lifes,(700,50))
        collides4 = sprite.spritecollide(rocket, astrorocks, True)
        collides3 = sprite.spritecollide(rocket, enemies, True)
        collides2 = sprite.groupcollide(astrorocks,bullets,False,True)
        collides1 = sprite.groupcollide(enemies,bullets,True,True)
        for c in collides1:
            destroy_score += 1
            enemy = EnemySprite('ufo.png',randint(0,750),0,uniform(1,2))
            enemies.add(enemy)
        for f in collides3:
            lifes = lifes - 1
            lost = lost + 1
            enemy = EnemySprite('ufo.png',randint(0,750),0,uniform(1,2))
            enemies.add(enemy)
        for d in collides4:
            lifes = lifes - 1
            astrorock = AstroSprite('asteroid.png',randint(0,750),0,randint(1,2))
            astrorocks.add(astrorock)
        text_destroyed = font2.render('Уничтожено: '+ str(destroy_score),1,(255,255,255))
        window.blit(text_destroyed,(15,25))
        if keys_pressed[K_SPACE] and pytime.time() - old_time > 0.6:
            rocket.spawn_bullet()
            shot.play()
            old_time = pytime.time()
        bullets.draw(window)
        bullets.update()
        astrorocks.draw(window)
        astrorocks.update()
        enemies.draw(window)
        enemies.update()
        rocket.draw(window)
        rocket.update()
        if destroy_score > 49:
            window.blit(text_win,(100,272))
            finish = True
        if lost > 5:
            window.blit(text_proigral,(100,272))
            finish = True
        if lifes < 1:
            window.blit(text_proigral,(100,272))
            finish = True
        display.update()
        clock.tick(FPS)











