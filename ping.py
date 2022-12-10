from pygame import*
import time as tm

W_W = 700
W_H = 500

window = display.set_mode((W_W, W_H))
window.fill(( 0, 0, 255))
game = True
clock = time.Clock()
class Sprite(sprite.Sprite):
    def __init__(self, fn, x, y, w, h, speedx, speedy):
        self.image = image.load(fn)
        self.image = transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.w = w
        self.h = h
        self.speedx = speedx
        self.speedy = speedy
    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Balls(Sprite):
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.y >= W_H or self.rect.y <= 0:
            self.speedy *= -1
        if self.rect.x >= W_W or self.rect.x <= 0:
            self.speedx *= -1
        super().update()

#Сделать клавиши для 2 игрока
class Player(Sprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y + self.speedy > 0 :
            self.rect.y -= self.speedy
        elif key_pressed[K_DOWN] and self.rect.y - self.w - self.speedy < W_H:
            self.rect.y += self.speedy
        super().update()


ball = Balls('лол.jpg', 0, 0, 30, 30, 3, 3)
Gamer1 = Player('GOC.jpg', 40, 0, 20, 70, 4, 4)
Gamer2 = Player('GOC.jpg', 640, 0, 20, 70, 4, 4)

while game:
    clock.tick(60)
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill(( 0, 0, 255))
    ball.update()
    Gamer1.update()
    Gamer2.update()
    
    display.update()
