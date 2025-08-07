from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_left (self):
        keys = key.get_pressed()
        if keys [K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 80:
            self.rect.y += self.speed

    def update_right (self):
        keys = key.get_pressed()
        if keys [K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - 80:
            self.rect.y += self.speed
    

win_width = 700
win_height = 500
#create game window
window = display.set_mode((700, 500))
display.set_caption('Ping pong R vs L')
# background = transform.scale(image.load('background.jpg'), (700, 500))



RIGHT = Player('racket.png', 640, 200, 4, 50, 90)
LEFT = Player ('racket.png', 5, 200, 4, 50, 90)
ball = GameSprite('bola.png', 300, 200, 0, 65, 65)
speed_x = 5
speed_y = 5

font.init()
font = font.Font(None, 70)
win = font.render('YOU WINN !!', True, (255, 215, 0))
lose = font.render('YOU LOSE :(', True, (180, 0, 0))

#set scene background
x1 = 100
y1 = 300

x2 = 300
y2 = 300

#handle "click on the "Close the window"" event 
finish = False
game = True
clock = time.Clock()
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
       window.fill((229, 204, 255))
       RIGHT.update_right()
       LEFT.update_left()
       ball.rect.x += speed_x
       ball.rect.y += speed_y
      
       RIGHT.reset()
       LEFT.reset()
       ball.reset()


    #    if sprite.collide_rect(packman, monster) or sprite.collide_rect(packman, w1)or sprite.collide_rect(packman, w2) or sprite.collide_rect(packman, w3) or sprite.collide_rect(packman, w4) or sprite.collide_rect(packman, w5) or sprite.collide_rect(packman, w6) or sprite.collide_rect(packman, w7):
    #        window.blit(lose, (200, 200))  
    #        finish = True
    #        kick.play()

    #    if sprite.collide_rect(packman, final):
    #        window.blit(win, (200, 200))  
    #        finish = True
    #        money.play()


    display.update()
    clock.tick(60)